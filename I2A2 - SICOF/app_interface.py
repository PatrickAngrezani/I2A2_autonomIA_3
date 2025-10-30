from datetime import datetime
import streamlit as st
import pandas as pd
import numpy as np
import warnings
from pydantic import BaseModel

# --- Importações do SICOF ---
from ingestion.xml_parser import xml_to_dataframe
from models.classification.classifier import predict_classification
from models.anomaly_detection.detector import predict_anomalies
from llm_agent.grouping_agent import group_expense

# --- Adições para ZIP ---
import zipfile
from io import BytesIO

# --- Fim Adições ---
from utils.utils import get_ramo_from_cnae
from utils.utils import execute_custom_action, CNAE_TO_RAMO_MAP

warnings.filterwarnings("ignore")


# --- Funções Auxiliares ---
def determine_doc_type(
    cfop: str, natureza_ia: str | None, categoria_ml: str | None
) -> str:
    """
    Determina se é Compra, Venda ou Serviço baseado no CFOP e classificações.
    Versão robusta para lidar com valores None.
    """
    cfop_str = (
        str(cfop).strip() if cfop is not None else ""
    )  # Garante string e trata None
    if not cfop_str:
        return "Tipo Indefinido"

    cfop_prefix = cfop_str[0]

    if cfop_prefix in ["1", "2", "3"]:
        return "Compra"
    elif cfop_prefix in ["5", "6", "7"]:
        natureza_lower = natureza_ia.lower() if natureza_ia != "None" else ""
        # Verifica se categoria_ml é uma string válida antes de usar .lower()
        categoria_lower = str(categoria_ml).lower() if categoria_ml is not None else ""

        if "serviço" in natureza_lower or "serviços" in categoria_lower:
            return "Servico"
        else:
            return "Venda"

    return "Tipo Indefinido"


st.set_page_config(
    page_title="SICOF - Análise Fiscal Inteligente", page_icon="🤖", layout="wide"
)

st.title("SICOF - Sistema Inteligente de Classificação e Otimização Fiscal")
st.markdown("Faça o upload de um arquivo XML de NF-e ou NFS-e para análise completa.")

# --- Componente de Upload ---
uploaded_files = st.file_uploader(
    "Selecione os arquivos XML",
    type=["xml"],
    accept_multiple_files=True,  # Permite múltiplos arquivos
)

zip_buffer = None


if uploaded_files:
    st.info(f"{len(uploaded_files)} arquivo(s) selecionado(s).")

    if st.button("Analisar Nota Fiscal"):

        all_results = []
        # --- Criar arquivo ZIP em memória ---
        zip_buffer_io = BytesIO()
        with zipfile.ZipFile(zip_buffer_io, "w", zipfile.ZIP_DEFLATED) as zipf:
            progress_bar = st.progress(0, text="Iniciando análise...")

            for i, uploaded_file in enumerate(uploaded_files):
                file_name = uploaded_file.name
                progress_text = (
                    f"Processando: {file_name} ({i+1}/{len(uploaded_files)})"
                )
                progress_bar.progress((i + 1) / len(uploaded_files), text=progress_text)

                result_data = {
                    "file_name": file_name,
                    "error": None,
                    "analysis": None,
                    "archive_zip_path": None,
                }

                try:
                    xml_content_bytes = uploaded_file.getvalue()  # Pega os bytes
                    xml_content_str = xml_content_bytes.decode(
                        "utf-8"
                    )  # Decodifica para string
                    df = xml_to_dataframe(xml_content_str)
                    
                    if df.empty:
                        result_data["error"] = "Não foi possível extrair dados do XML."
                        st.warning(f"Arquivo {file_name}: {result_data['error']}")
                        all_results.append(result_data)
                        continue

                    extracted_data = df.to_dict("records")[0]
                    descricao_item = extracted_data.get("descricao_item", "")
                    cnae_emitente = extracted_data.get("cnae_emitente")
                    cfop = extracted_data.get("cfop", "")

                    ramo_atividade_detectado = get_ramo_from_cnae(cnae_emitente)

                    class_preds, class_probs = predict_classification(df)
                    anomaly_preds, anomaly_scores = predict_anomalies(df)
                    grouping_result = group_expense(
                        descricao_item, ramo_atividade_detectado
                    )
                    custom_results = execute_custom_action(
                        ramo_atividade_detectado, extracted_data
                    )

                    categoria_ml = class_preds[0] if class_preds is not None else ""
                    natureza_ia = (
                        grouping_result.natureza_despesa if grouping_result else ""
                    )
                    centro_custo_ia = (
                        grouping_result.centro_custo
                        if grouping_result
                        else "Indefinido"
                    )
                    doc_type = determine_doc_type(cfop, natureza_ia, categoria_ml)
                    centro_custo_folder = (
                        centro_custo_ia.replace("/", "-").replace("\\", "-").strip()
                        if centro_custo_ia
                        else "Indefinido"
                    )
                    # Garante nomes de pasta válidos (simplificado)
                    doc_type_folder = (
                        "".join(
                            c for c in doc_type if c.isalnum() or c in (" ", "_")
                        ).rstrip()
                        or "Indefinido"
                    )
                    centro_custo_folder = (
                        "".join(
                            c
                            for c in centro_custo_folder
                            if c.isalnum() or c in (" ", "_")
                        ).rstrip()
                        or "Indefinido"
                    )

                    # --- Define o caminho DENTRO do ZIP ---
                    # Usando barras normais para compatibilidade entre OS no ZIP
                    archive_zip_path = (
                        f"{doc_type_folder}/{centro_custo_folder}/{file_name}"
                    )
                    print(f"Adicionando '{file_name}' ao ZIP em: {archive_zip_path}")
                    # Adiciona o arquivo XML (bytes originais) ao ZIP
                    zipf.writestr(archive_zip_path, xml_content_bytes)
                    # --- Fim da Lógica do ZIP ---

                    result_data["analysis"] = {
                        "extracted_data": extracted_data,
                        "ramo": ramo_atividade_detectado,
                        "classification": (
                            class_preds[0] if class_preds is not None else "N/A",
                            np.max(class_probs[0]) if class_probs is not None else 0.0,
                        ),
                        "anomaly": (
                            anomaly_preds[0] if anomaly_preds is not None else None,
                            anomaly_scores[0] if anomaly_scores is not None else 0.0,
                        ),
                        "grouping": grouping_result,
                        "custom_actions": custom_results,
                        "doc_type": doc_type,
                        "centro_custo_ia": centro_custo_ia,
                    }
                    result_data["archive_zip_path"] = (
                        archive_zip_path  # Caminho dentro do ZIP
                    )
                    all_results.append(result_data)
                    print(f"Análise de {file_name} concluída.")

                except Exception as e:
                    result_data["error"] = f"Erro inesperado: {e}"
                    st.error(f"Ocorreu um erro ao analisar {file_name}: {e}")
                    st.exception(e)
                    all_results.append(result_data)

            progress_bar.progress(1.0, text="Análise e preparação do ZIP concluída!")

        # --- Armazena o buffer do ZIP para o botão de download ---
        zip_buffer = zip_buffer_io.getvalue()
        st.session_state["zip_buffer"] = zip_buffer  # Salva no estado da sessão
        st.session_state["all_results"] = all_results  # Salva resultados também

# --- Exibição dos Resultados (Usa o estado da sessão) ---
# Verifica se há resultados guardados na sessão
if "all_results" in st.session_state and st.session_state["all_results"]:
    all_results = st.session_state["all_results"]  # Carrega os resultados da sessão
    st.divider()
    st.header("Resultados da Análise em Lote")

    # Contagem de sucessos e falhas
    successful_files = [r for r in all_results if r.get("analysis") is not None]
    failed_files = [r for r in all_results if r.get("error") is not None]

    st.success(f"**{len(successful_files)} arquivo(s) pronto(s) para arquivamento.**")
    if failed_files:
        st.error(f"**{len(failed_files)} arquivo(s) falharam na análise.**")

    # --- Botão de Download (Usa o buffer da sessão) ---
    if "zip_buffer" in st.session_state and st.session_state["zip_buffer"]:
        st.download_button(
            label="⬇️ Baixar Arquivo ZIP com XMLs Organizados",
            data=st.session_state["zip_buffer"],
            file_name=f"SICOF_Arquivados_{datetime.now().strftime('%Y%m%d_%H%M%S')}.zip",
            mime="application/zip",
            key="download_zip_button",
        )

    # --- Loop para exibir detalhes de cada arquivo ---
    st.markdown("---")  # Divisor antes dos detalhes
    for result in all_results:
        # Define o título do expander
        expander_label = f"{result.get('file_name', 'Nome Desconhecido')} - Status: {'Sucesso' if result.get('analysis') else 'Falha'}"

        # Cria o expander para cada resultado
        with st.expander(expander_label):
            # Verifica se a análise foi bem-sucedida
            if result.get("analysis"):
                analysis = result["analysis"]
                extracted = analysis.get(
                    "extracted_data", {}
                )  # Pega o dict de dados extraídos

                st.subheader(f"Detalhes: {result.get('file_name', 'N/A')}")
                st.info(
                    f"Arquivamento ZIP: `{result.get('archive_zip_path', 'N/A')}` (Tipo: {analysis.get('doc_type', 'N/A')}, C. Custo: {analysis.get('centro_custo_ia', 'N/A')})"
                )

                # --- Visão Geral (Métricas Principais) ---
                col1, col2, col3 = st.columns(3)
                with col1:  # Classificação ML
                    class_val = analysis.get("classification", ("N/A", 0.0))
                    st.metric(
                        label="Classificação ML",
                        value=str(class_val[0]),
                        delta=f"{class_val[1]*100:.2f}% conf",
                    )
                with col2:  # Anomalia ML
                    anom_val = analysis.get("anomaly", (None, 0.0))
                    eh_anomalia = (
                        (anom_val[0] == -1) if anom_val[0] is not None else False
                    )
                    score = anom_val[1]
                    label_anomalia = "Anomalia ML"
                    if eh_anomalia:
                        st.metric(
                            label=label_anomalia,
                            value="DETECTADA",
                            delta_color="inverse",
                        )
                        st.caption(f"Score: {score:.4f}")
                    else:
                        st.metric(
                            label=label_anomalia, value="Normal", delta_color="off"
                        )
                        st.caption(f"Score: {score:.4f}")
                with col3:  # Centro Custo IA
                    grouping_val = analysis.get("grouping")
                    centro_custo_display = "N/A"
                    if grouping_val and isinstance(grouping_val, BaseModel):
                        centro_custo_display = grouping_val.centro_custo
                    st.metric(label="Centro Custo (IA)", value=centro_custo_display)

                st.divider()  # Separa visão geral dos detalhes

                # --- Detalhes Divididos (Fiscal e IA/Custom) ---
                col_fiscal, col_ia_custom = st.columns([3, 2])  # Coluna fiscal maior

                # --- Coluna Detalhes Fiscais (Aprimorada) ---
                with col_fiscal:
                    st.markdown("**Detalhes Fiscais e do Produto/Serviço**")

                    # Usando st.text ou st.caption para códigos e descrições
                    # Usando .get() com valor padrão 'N/A' para segurança
                    st.text(
                        f"Produto/Serviço: {extracted.get('descricao_item', 'N/A')}"
                    )

                    # Subcolunas para organização
                    col_f1, col_f2 = st.columns(2)
                    with col_f1:
                        st.text(f"CFOP: {extracted.get('cfop', 'N/A')}")
                        st.text(f"Emitente: {extracted.get('cnpj_emitente', 'N/A')}")
                        st.text(
                            f"CNAE Emitente: {extracted.get('cnae_emitente', 'N/A')}"
                        )
                    with col_f2:
                        st.text(f"NCM: {extracted.get('ncm', 'N/A')}")
                        st.text(
                            f"Destinatário: {extracted.get('cnpj_destinatario', 'N/A')}"
                        )
                        # Adicione outros campos se o parser os extrair (ex: IE)
                        # st.text(f"IE Emitente: {extracted.get('ie_emitente', 'N/A')}")

                    st.divider()  # Separa códigos dos valores
                    st.markdown("**Valores Monetários:**")

                    # Subcolunas para valores
                    col_v1, col_v2, col_v3 = st.columns(3)
                    with col_v1:
                        # Formata valores como moeda brasileira BRL
                        valor_nf = extracted.get("valor_total_nf", 0)
                        st.metric(
                            "Total NF",
                            f"R$ {valor_nf:,.2f}" if valor_nf is not None else "N/A",
                        )
                    with col_v2:
                        valor_icms = extracted.get("valor_icms", 0)
                        st.metric(
                            "ICMS",
                            (
                                f"R$ {valor_icms:,.2f}"
                                if valor_icms is not None
                                else "N/A"
                            ),
                        )
                    with col_v3:
                        ipi = extracted.get("valor_ipi")
                        # Mostra IPI apenas se existir (não for None)
                        if ipi is not None:
                            st.metric("IPI", f"R$ {ipi:,.2f}")
                        else:
                            # Se for None, indica que não foi encontrado
                            st.metric("IPI", "N/A")

                # --- Coluna IA e Ações Customizadas (Mantida) ---
                with col_ia_custom:
                    st.markdown("**Agrupamento (IA)**")
                    st.caption(
                        f"Ramo Inferido: {analysis.get('ramo', 'N/A')}"
                    )  # Usa .get()
                    grouping_val = analysis.get("grouping")
                    if grouping_val and isinstance(grouping_val, BaseModel):
                        st.json(
                            {
                                "Centro de Custo": grouping_val.centro_custo,
                                "Natureza da Despesa": grouping_val.natureza_despesa,
                                "Finalidade": grouping_val.finalidade,
                            }
                        )
                    else:
                        st.warning("Não foi possível obter o agrupamento da IA.")

                    st.markdown("**Verificações Específicas**")
                    custom_results = analysis.get("custom_actions")  # Usa .get()
                    if custom_results and isinstance(
                        custom_results, dict
                    ):  # Verifica se é dict
                        if custom_results.get("info"):
                            for msg in custom_results["info"]:
                                st.info(f"- {msg}")
                        if custom_results.get("warnings"):
                            for msg in custom_results["warnings"]:
                                st.warning(f"- {msg}")
                    elif custom_results:  # Se não for dict mas existir
                        st.write(f"Resultado inesperado: {custom_results}")
                    else:  # Se for None ou vazio
                        st.caption(
                            "Nenhuma verificação específica executada ou configurada."
                        )

            # Caso a análise tenha falhado (error is not None)
            elif result.get("error"):
                st.error(
                    f"**Erro ao processar {result.get('file_name', 'N/A')}**: {result['error']}"
                )

# Limpa o estado se não houver mais arquivos carregados
elif (
    not uploaded_files
    and "all_results" in st.session_state
    and st.session_state["all_results"]
):
    st.session_state["all_results"] = []
    st.session_state["zip_buffer"] = None
    print("Limpando estado da sessão.")
    st.rerun()
