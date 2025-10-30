import pandas as pd
import numpy as np
from ingestion.xml_parser import xml_to_dataframe, parse_nfe_xml
from models.classification.classifier import train_classifier, predict_classification
from models.anomaly_detection.detector import train_anomaly_detector, predict_anomalies
from llm_agent.grouping_agent import group_expense
from utils.utils import execute_custom_action, get_ramo_from_cnae
from validation.metrics import calculate_classification_metrics
import warnings

warnings.filterwarnings("ignore")


def create_simulated_dataset(size=100) -> (pd.DataFrame, pd.Series):
    """
    Cria uma base de dados simulada (anonimizada) para o protótipo.
    """
    print(f"Gerando {size} amostras de dados simulados...")
    data = {
        "cnpj_emitente": [
            f"{np.random.randint(10**13, 10**14-1, dtype=np.int64):014d}"
            for _ in range(size)
        ],
        "cnpj_destinatario": [
            f"{np.random.randint(10**13, 10**14-1, dtype=np.int64):014d}"
            for _ in range(size)
        ],
        "cfop": np.random.choice(["5102", "6102", "5405", "1102"], size=size),
        "ncm": np.random.choice(
            ["85234990", "39269090", "48201000", "90011019"], size=size
        ),
        "descricao_item": np.random.choice(
            [
                "SERVICO DE CONSULTORIA EM TI",
                "AQUISICAO DE MATERIAL DE ESCRITORIO",
                "SERVICO DE LIMPEZA PREDIAL",
                "COMPRA DE PECAS DE COMPUTADOR",
                "MANUTENCAO DE AR CONDICIONADO",
            ],
            size=size,
        ),
        "valor_total_nf": np.random.uniform(100, 50000, size=size),
        "valor_icms": lambda df_row: df_row["valor_total_nf"]
        * np.random.uniform(0.12, 0.18),
    }

    df = pd.DataFrame(data)
    df["valor_icms"] = df.apply(data["valor_icms"], axis=1).round(2)

    def map_target(desc):
        if "SERVICO" in desc or "MANUTENCAO" in desc:
            return "Serviços"
        return "Material de Consumo"

    y = df["descricao_item"].apply(map_target)

    return df, y


def run_full_pipeline():
    """
    treinamento -> Validação -> Inferência.
    """

    print("inicia treinamento")

    X_train, y_train = create_simulated_dataset(size=200)

    train_classifier(X_train, y_train)
    train_anomaly_detector(X_train)

    print("etapa de validação")
    X_test, y_test = create_simulated_dataset(size=50)

    preds, _ = predict_classification(X_test)
    if preds is not None:
        calculate_classification_metrics(y_test, preds)

    print("etapa de inferencia")

    # carrega xml
    with open("data/example.xml", "r", encoding="utf-8") as f:
        xml_string = f.read()

    # converte xml
    new_invoice_df = xml_to_dataframe(xml_string)

    extracted_data = new_invoice_df.to_dict("records")[0]
    print(f"Dados extraídos do XML: {pd.Series(extracted_data).to_string()}")

    # classifica 
    class_pred, class_prob = predict_classification(new_invoice_df)
    
    # nessa parte se faz interessante organizar e arquivar os arquivos

    # detecta nomalias
    anomaly_pred, anomaly_score = predict_anomalies(new_invoice_df)

    print(f"score de anomalia: {anomaly_score[0]:.4f}")

    # executa Agente de IA (LLM)
    print("\n[Módulo de Agente de IA (LLM)]")
    descricao_item = new_invoice_df["descricao_item"].iloc[0]
    cnae_emitente_extraido = (
        new_invoice_df["cnae_emitente"].iloc[0]
        if "cnae_emitente" in new_invoice_df.columns
        else None
    )
    ramo_atividade_detectado = get_ramo_from_cnae(cnae_emitente_extraido)
    grouping = group_expense(descricao_item, ramo_atividade_detectado)
    print(f"centro de Custo: {grouping.centro_custo}")
    print(f"natureza da Despesa: {grouping.natureza_despesa}")
    print(f"finalidade: {grouping.finaliedade}")

    # ação customizada
    print("\n[Módulo de Ações Customizadas]")
    custom_results = execute_custom_action(ramo_atividade_detectado, extracted_data)
    if custom_results:
        for level, messages in custom_results.items():
            if messages:
                print(f"  > {level.capitalize()}:")
                for msg in messages:
                    print(f"    - {msg}")
    else:
        print("nenhuma ação customizada executada.")

    print("\n--- PIPELINE DE INFERÊNCIA COMPLETO ---")


if __name__ == "__main__":
    # Verifica se a chave de IA está configurada antes de rodar
    from config.settings import settings

    if settings.OPENAI_API_KEY == "CHAVE_NAO_ENCONTRADA":
        print("=" * 50)
        print("ERRO: OPENAI_API_KEY não configurada.")
        print("Por favor, crie o arquivo .env e adicione sua chave.")
        print("=" * 50)
    else:
        run_full_pipeline()
