# SICOF - Sistema Inteligente de Classificação e Otimização Fiscal

Este é um protótipo funcional do SICOF, um sistema em Python para classificação, análise de anomalias e interpretação de notas fiscais eletrônicas (NF-e/NFS-e) usando Machine Learning e Agentes de IA, conforme especificado nos requisitos do projeto.

## Arquitetura

O projeto é dividido nos seguintes módulos:
- `/ingestion`: Parse de dados de XML.
- `/preprocessing`: Pipelines de limpeza e transformação de dados.
- `/models`: Módulos de ML para classificação e detecção de anomalias.
- `/llm_agent`: Agente de IA (LLM) para interpretação e agrupamento.
- `/api`: API REST (FastAPI) para expor o sistema.
- `/validation`: Funções para calcular métricas de performance.
- `/config`: Gerenciamento de configurações.

## 1. Configuração do Ambiente

### a. Crie um Ambiente Virtual
```bash
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
```

### b. Instale as dependências
 ```bash
pip install -r requirements.txt
```

## 2. Execução do Sistema

### Iniciar a interface web via Streamlit:
```bash
streamlit run app_interface.py
```

## 🌐 Aplicação Online  

Acesse a versão hospedada no **Streamlit Cloud**:  

[🔗 **SICOF no Streamlit**](https://i2a2autonomia3-hfg8zvjkfcykuekcvdzmwv.streamlit.app/)
