import pandas as pd
from lxml import etree
from io import BytesIO

def parse_nfe_xml(xml_content: str) -> dict:
    xml_bytes = xml_content.encode('utf-8')
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
            clean_path = './/' + path.split('}')[-1] if '}' in path else path
            node = root.find(clean_path, namespaces=None)
        return node.text.strip() if node is not None and node.text is not None else None

    cnpj_dest = find_text('.//dest/CNPJ')
    cpf_dest = find_text('.//dest/CPF') 

    destinatario_id = cnpj_dest if cnpj_dest is not None else cpf_dest
    print(cnpj_dest, cpf_dest, destinatario_id)

    data = {
        'cnpj_emitente': find_text('.//emit/CNPJ'),
        'cnpj_destinatario': destinatario_id,
        'cnae_emitente': find_text('.//emit/CNAE'),
        'cfop': find_text('.//det/prod/CFOP'),
        'ncm': find_text('.//det/prod/NCM'),
        'descricao_item': find_text('.//det/prod/xProd'),
        'valor_total_nf': find_text('.//total/ICMSTot/vNF'),
        'valor_icms': find_text('.//total/ICMSTot/vICMS'),
        'valor_ipi': find_text('.//det/imposto/IPI/vIPI')
    }
    return data

def xml_to_dataframe(xml_content: str) -> pd.DataFrame:
    """Converte os dados extraídos do XML para um DataFrame."""
    data = parse_nfe_xml(xml_content)
    if not data:
         print("Parse do XML retornou vazio. Criando DataFrame vazio.")
         return pd.DataFrame()

    df = pd.DataFrame([data])

    string_cols = ['cnpj_emitente', 'cnpj_destinatario', 'cnae_emitente', 'cfop', 'ncm']
    for col in string_cols:
        if col in df.columns:
            # fillna('') antes de astype(str) para evitar converter None para "None"
            df[col] = df[col].fillna('').astype(str).str.strip()

    numeric_cols = ['valor_total_nf', 'valor_icms', 'valor_ipi']
    for col in numeric_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce')

    return df
