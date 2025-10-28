import streamlit as st
import pandas as pd
import numpy as np
import warnings

# --- Importações do SICOF ---
from ingestion.xml_parser import xml_to_dataframe
from models.classification.classifier import predict_classification
from models.anomaly_detection.detector import predict_anomalies
from llm_agent.grouping_agent import group_expense

from utils.utils import get_ramo_from_cnae
from utils.utils import execute_custom_action, CNAE_TO_RAMO_MAP

warnings.filterwarnings("ignore")

st.set_page_config(
    page_title="SICOF - Análise Fiscal Inteligente", page_icon="🤖", layout="wide"
)

st.title("SICOF - Sistema Inteligente de Classificação e Otimização Fiscal")
st.markdown("Faça o upload de um arquivo XML de NF-e ou NFS-e para análise completa.")

# --- Componente de Upload ---
uploaded_file = st.file_uploader("Selecione o arquivo XML", type=["xml"])

if uploaded_file is not None:
    if st.button("Analisar Nota Fiscal"):

        with st.spinner(
            "Processando... Lendo XML, executando modelos de ML e consultando IA..."
        ):
            try:
                xml_content = uploaded_file.getvalue().decode("utf-8")

                df = xml_to_dataframe(xml_content)
                if df.empty:
                    st.error("Não foi possível extrair dados do XML.")
                else:
                    extracted_data = df.to_dict("records")[0]
                    descricao_item = extracted_data.get("descricao_item", "")
                    cnae_emitente = extracted_data.get("cnae_emitente")  # Pega o CNAE

                    #  ramo
                    ramo_atividade_detectado = get_ramo_from_cnae(cnae_emitente)
                    st.info(
                        f"CNAE Emitente detectado: {cnae_emitente if cnae_emitente else 'Não encontrado'} -> Ramo Inferido: {ramo_atividade_detectado}"
                    )  # Mostra na interface

                    # predições
                    class_preds, class_probs = predict_classification(df)
                    anomaly_preds, anomaly_scores = predict_anomalies(df)
                    grouping_result = group_expense(
                        descricao_item, ramo_atividade_detectado
                    )

                    custom_results = execute_custom_action(
                        ramo_atividade_detectado, extracted_data
                    )

                    st.success("Análise Concluída!")

                    st.subheader("Visão Geral da Análise")
                    col1, col2, col3 = st.columns(3)
                    with col1:
                        categoria = class_preds[0] if class_preds is not None else "N/A"
                        confianca = (
                            np.max(class_probs[0]) if class_probs is not None else 0.0
                        )
                        st.metric(
                            label="Classificação ML",
                            value=str(categoria),
                            delta=f"{confianca*100:.2f}% conf",
                        )
                    with col2:
                        eh_anomalia = (
                            (anomaly_preds[0] == -1)
                            if anomaly_preds is not None
                            else False
                        )
                        score = anomaly_scores[0] if anomaly_scores is not None else 0.0
                        if eh_anomalia:
                            st.metric(label="Anomalia ML", value="DETECTADA")
                            st.error(f"Score: {score:.4f}")
                        else:
                            st.metric(label="Anomalia ML", value="Normal")
                            st.success(f"Score: {score:.4f}")
                    with col3:  # Centro de Custo IA
                        st.metric(
                            label="Centro Custo (IA)",
                            value=(
                                grouping_result.centro_custo
                                if grouping_result
                                else "N/A"
                            ),
                        )

                    st.divider()

                    col_ia, col_dados = st.columns([2, 3])

                    with col_ia:
                        st.subheader("Agrupamento por Agente de IA")
                        st.info(
                            f"**Ramo Considerado:** {ramo_atividade_detectado if ramo_atividade_detectado else 'Não informado/Geral'}"
                        )
                        st.info(f"**Descrição Analisada:** {descricao_item}")
                        if grouping_result:
                            st.json(
                                {
                                    "Centro de Custo": grouping_result.centro_custo,
                                    "Natureza da Despesa": grouping_result.natureza_despesa,
                                    "Finalidade (Resumo)": grouping_result.finalidade,
                                }
                            )
                        else:
                            st.warning("Não foi possível obter o agrupamento da IA.")

                        st.divider()
                        st.subheader(
                            f"⚙️ Verificações Específicas: {ramo_atividade_detectado if ramo_atividade_detectado else 'Geral'}"
                        )
                        if custom_results:
                            if custom_results.get("info"):
                                st.markdown("**Informações:**")
                                for msg in custom_results["info"]:
                                    st.info(f"- {msg}")
                            if custom_results.get("warnings"):
                                st.markdown("**Avisos:**")
                                for msg in custom_results["warnings"]:
                                    st.warning(f"- {msg}")
                        else:
                            st.write(
                                "Nenhuma verificação específica para este ramo foi configurada ou executada."
                            )

                    with col_dados:
                        st.subheader("Dados Extraídos do XML")
                        st.dataframe(df)

            except Exception as e:
                st.error(f"Ocorreu um erro durante a análise: {e}")
                st.exception(e)
