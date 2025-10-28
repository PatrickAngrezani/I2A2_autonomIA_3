from fastapi import FastAPI, HTTPException
import numpy as np
import pandas as pd

from api.schemas import (
    InvoiceInput,
    AnalysisResponse,
    ClassificationOutput,
    AnomalyOutput,
    GroupingOutput,
)
from ingestion.xml_parser import xml_to_dataframe
from models.classification.classifier import predict_classification
from models.anomaly_detection.detector import predict_anomalies
from llm_agent.grouping_agent import group_expense

from utils.utils import (
    execute_custom_action,
    CNAE_TO_RAMO_MAP,
    get_ramo_from_cnae,
)

print("Módulos de ações customizadas importados com sucesso.")

app = FastAPI(
    title="SICOF - API de Análise Fiscal",
    description="API para classificação, detecção de anomalias, agrupamento e ações customizadas de notas fiscais.",
)


@app.get("/", summary="Verifica o status da API")
def read_root():
    """Endpoint raiz para verificar se a API está online."""
    return {"status": "SICOF API está operacional"}


@app.post(
    "/analyze",
    response_model=AnalysisResponse,
    summary="Executa a análise fiscal completa em um XML",
)
async def analyze_invoice(invoice: InvoiceInput):
    """
    Recebe o conteúdo de um XML de NF-e/NFS-e e executa o pipeline de análise:
    1.  Parse do XML (extraindo CNAE)
    2.  Predição de Classificação (ML)
    3.  Predição de Anomalia (ML)
    4.  Determinação do Ramo de Atividade (via CNAE)
    5.  Agrupamento Inteligente (LLM considerando o Ramo)
    6.  Execução de Ações Customizadas (baseado no Ramo)
    """
    print("\n--- Recebida nova requisição /analyze ---")
    try:
        # parse do XML
        df = xml_to_dataframe(invoice.xml_content)
        if df.empty:
            print("ERRO: Falha ao extrair dados do XML.")
            raise HTTPException(
                status_code=400, detail="Não foi possível extrair dados do XML."
            )

        # converte para dict para facilitar o acesso
        extracted_data = df.to_dict("records")[0]
        descricao_item = extracted_data.get("descricao_item", "")
        cnae_emitente = extracted_data.get("cnae_emitente")  # Pega o CNAE extraído
        print(f"Dados extraídos: {extracted_data}")

    except Exception as e:
        print(f"ERRO durante o parse: {e}")
        raise HTTPException(status_code=400, detail=f"Erro no parse do XML: {e}")

    try:
        # predição de Classificação
        class_preds, class_probs = predict_classification(df)
        categoria = "Erro na predição"
        confianca = 0.0
        if class_preds is not None and class_probs is not None:
            categoria = class_preds[0]
            # Garante que class_probs[0] seja iterável antes de np.max
            if hasattr(class_probs[0], "__iter__"):
                confianca = np.max(class_probs[0])
            elif isinstance(class_probs[0], (int, float)):  # Caso de classe única?
                confianca = class_probs[0]

        class_output = ClassificationOutput(
            categoria_predita=str(categoria), confianca=float(confianca)
        )
        print(f"Classificação: {class_output}")

        # predição de Anomalia
        anomaly_preds, anomaly_scores = predict_anomalies(df)
        eh_anomalia = False
        score = 0.0
        if anomaly_preds is not None and anomaly_scores is not None:
            eh_anomalia = anomaly_preds[0] == -1
            score = anomaly_scores[0]

        anomaly_output = AnomalyOutput(
            eh_anomalia=bool(eh_anomalia), score_anomalia=float(score)
        )
        print(f"Anomalia: {anomaly_output}")

        # ramo de Atividade
        ramo_atividade = get_ramo_from_cnae(cnae_emitente)
        print(f"ramo determinado a partir do CNAE: {ramo_atividade}")

        grouping_result = group_expense(descricao_item, ramo_atividade)
        grouping_output = None
        if grouping_result and isinstance(grouping_result, BaseModel):
            grouping_output = GroupingOutput(**grouping_result.dict())
        else:
            print(
                f"AVISO: Agrupamento LLM não retornou resultado esperado: {grouping_result}"
            )
            grouping_output = GroupingOutput(
                centro_custo="N/A", natureza_despesa="N/A", finalidade="Falha na IA"
            )
        print(f"agrupamento IA: {grouping_output}")

        # ação customizada
        print("Executando ações customizadas...")
        custom_results = execute_custom_action(ramo_atividade, extracted_data)
        print(f"Resultados customizados: {custom_results}")

        # 7. Montar Resposta Final
        print("Montando resposta final da API.")
        return AnalysisResponse(
            dados_extraidos=extracted_data,
            classificacao=class_output,
            anomalia=anomaly_output,
            agrupamento_ia=grouping_output,
            acoes_customizadas=custom_results,  # Adiciona resultado customizado
            status="Análise concluída com sucesso",
        )

    except FileNotFoundError as fnf_error:
        # Erro específico se os modelos .joblib não forem encontrados
        print(f"ERRO FATAL: Modelo ML não encontrado: {fnf_error}")
        raise HTTPException(
            status_code=500,
            detail=f"Erro: Modelo ML não treinado ou não encontrado ({fnf_error}). Execute o script de treinamento.",
        )
    except Exception as e:
        # Pega outras exceções durante a análise ML ou LLM
        print(f"ERRO durante a análise: {e}")
        import traceback

        traceback.print_exc()  # Imprime o traceback completo no console do servidor para debug
        raise HTTPException(
            status_code=500, detail=f"Erro interno durante a análise: {e}"
        )


# --- Ponto de entrada para uvicorn (se executar este arquivo diretamente) ---
# Em produção, é melhor usar o comando uvicorn diretamente
if __name__ == "__main__":
    import uvicorn

    print("Iniciando servidor FastAPI em http://127.0.0.1:8000")
    # Verifica se a chave de IA está configurada
    try:
        from config.settings import settings

        if settings.OPENAI_API_KEY == "CHAVE_NAO_ENCONTRADA":
            print("\n" + "=" * 50)
            print("ERRO CRÍTICO: OPENAI_API_KEY não configurada no .env!")
            print("A funcionalidade de Agrupamento por IA não funcionará.")
            print("=" * 50 + "\n")
    except ImportError:
        print(
            "\nAVISO: Módulo 'config.settings' não encontrado. Verificação da API Key pulada.\n"
        )

    uvicorn.run(app, host="127.0.0.1", port=8000)
