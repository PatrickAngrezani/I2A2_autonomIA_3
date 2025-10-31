import re
import numpy as np
import pandas as pd
from lxml import etree
from io import BytesIO


def parse_nfe_xml(xml_content: str) -> dict:
    # Remove todos os namespaces (xmlns="...") da NF-e
    xml_sem_ns = re.sub(r'\sxmlns(:\w+)?="[^"]+"', "", xml_content)
    xml_bytes = xml_sem_ns.encode("utf-8")
    parser = etree.XMLParser(remove_blank_text=True, ns_clean=True, recover=True)

    try:
        tree = etree.parse(BytesIO(xml_bytes), parser)
        root = tree.getroot()
    except etree.XMLSyntaxError as e:
        print(f"Erro de sintaxe XML: {e}")
        return {}
    except Exception as e:
        print(f"Erro inesperado durante o parse do XML: {e}")
        return {}

    ns = {k: v for k, v in root.nsmap.items() if k}

    def find_text(path):
        node = root.find(path, namespaces=ns)
        if node is None:
            clean_path = ".//" + path.split("}")[-1] if "}" in path else path
            node = root.find(clean_path, namespaces=None)
        return node.text.strip() if node is not None and node.text is not None else None

    cnpj_dest = find_text(".//dest/CNPJ")
    cpf_dest = find_text(".//dest/CPF")
    valor_ipi_encontrado = find_text(".//det/imposto/IPI/IPITrib/vIPI") or find_text(
        ".//det/imposto/IPI/vIPI"
    )

    destinatario_id = cnpj_dest if cnpj_dest is not None else cpf_dest
    print(
        f"**12**cnpj_dest: {cnpj_dest}, **12**cpf_dest: {cpf_dest}, **12**destinatario_id: {destinatario_id}"
    )
    print(f"**124*valor_IPI: {valor_ipi_encontrado}")

    data = {
        "cnpj_emitente": find_text(".//emit/CNPJ"),
        "cnpj_destinatario": destinatario_id,
        "cnae_emitente": find_text(".//emit/CNAE"),
        "cfop": find_text(".//det/prod/CFOP"),
        "ncm": find_text(".//det/prod/NCM"),
        "descricao_item": find_text(".//det/prod/xProd"),
        "valor_total_nf": find_text(".//total/ICMSTot/vNF"),
        "valor_icms": find_text(".//total/ICMSTot/vICMS"),
        "valor_ipi": find_text(".//det/imposto/IPI/vIPI"),
    }
    return data


def xml_to_dataframe(xml_content: str) -> pd.DataFrame:
    """Converte os dados extraídos do XML para um DataFrame, aplicando tipagem correta."""
    data = parse_nfe_xml(xml_content)
    print(f"data_xml: {data}")

    if not data:  # Verifica se o parse retornou um dicionário vazio
        print("Parse do XML retornou vazio. Criando DataFrame vazio.")
        return pd.DataFrame()  # Retorna DataFrame vazio

    # Cria o DataFrame a partir do dicionário (que tem uma única linha)
    df = pd.DataFrame([data])

    # substitui valores nulos e espaços em branco nas colunas
    df = df.replace(r"^\s*$", np.nan, regex=True)
    df = df.replace(["None", None, "", "nan", "NaN", "NONE"], np.nan)


    string_cols = [
        "cnpj_emitente",
        "cnpj_destinatario",
        "cnae_emitente",
        "descricao_item",
    ]

    for col in string_cols:
        if col in df.columns:
            df[col] = (
                df[col]
                .astype(str)
                .str.strip()
            )

    numeric_cols = [
        "valor_total_nf",
        "valor_icms",
        "valor_ipi",
        "cfop",
        "ncm",
    ]
    for col in numeric_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")

    df[numeric_cols] = df[numeric_cols].fillna(0)

    # garante que as colunas tenham tipos compativeis
    for col in df.columns:
        if df[col].dtype == object:
            df[col] = df[col].astype(str)
        elif not np.issubdtype(df[col].dtype, np.number):
            df[col] = pd.to_numeric(df[col], errors="coerce").fillna(0)

    return df
