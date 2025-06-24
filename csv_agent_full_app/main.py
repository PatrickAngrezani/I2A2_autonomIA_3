import os
import zipfile
import pandas as pd
from dotenv import load_dotenv
from langchain_experimental.agents import create_csv_agent
from langchain.llms import OpenAI
import streamlit as st
import signal

load_dotenv()

# Define paths
ZIP_PATH = "data/202401_NFs.zip"
EXTRACT_PATH = "data/unzipped"

# Extract ZIP
with zipfile.ZipFile(ZIP_PATH, 'r') as zip_ref:
    zip_ref.extractall(EXTRACT_PATH)

# Look for CSV files in the extracted content
cab_path = None
item_path = None
for root, dirs, files in os.walk(EXTRACT_PATH):
    for file in files:
        name = file.lower()
        if "cabecalho" in name and file.endswith(".csv"):
            cab_path = os.path.join(root, file)
        elif ("item" in name or "itens" in name) and file.endswith(".csv"):
            item_path = os.path.join(root, file)

if not cab_path or not item_path:
    st.error("❌ Arquivos de cabeçalho ou itens não encontrados no ZIP.")
    st.stop()

# Load DataFrames
df_cab = pd.read_csv(cab_path)
df_item = pd.read_csv(item_path)

# Save temp CSVs for agent use
df_cab.to_csv("cabecalho_temp.csv", index=False)
df_item.to_csv("itens_temp.csv", index=False)

# Init LLM and agents
llm = OpenAI(temperature=0)
agent_cab = create_csv_agent(llm, "cabecalho_temp.csv", verbose=True, allow_dangerous_code=True)
agent_item = create_csv_agent(llm, "itens_temp.csv", verbose=True, allow_dangerous_code=True)

# Streamlit UI
st.set_page_config(page_title="Agente de Notas Fiscais ZIP", layout="wide")
st.title("📦 Agente de Consulta de Notas Fiscais (via ZIP)")

query = st.text_input("Pergunta (ex: Qual o valor total das notas para o DF?)")

if st.button("Consultar"):
    if query:
        st.subheader("📑 Cabeçalho:")
        st.write(agent_cab.run(query))

        st.subheader("📦 Itens:")
        st.write(agent_item.run(query))

# Botão para encerrar o agente (encerrar o Streamlit)
if st.button("🛑 Encerrar Agente"):
    st.warning("Encerrando completamente o agente e liberando o terminal...")
    os.kill(os.getpid(), signal.SIGTERM)
