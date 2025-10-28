CNAE_TO_RAMO_MAP = {
    # SEÇÃO A: AGRICULTURA, PECUÁRIA, PRODUÇÃO FLORESTAL, PESCA E AQÜICULTURA
    "01": "Agronegócio (Agricultura, Pecuária)",
    "02": "Agronegócio (Produção Florestal)",
    "03": "Agronegócio (Pesca e Aquicultura)",
    # SEÇÃO B: INDÚSTRIAS EXTRATIVAS
    "05": "Indústria Extrativa (Carvão Mineral)",
    "06": "Indústria Extrativa (Petróleo e Gás)",
    "07": "Indústria Extrativa (Minerais Metálicos)",
    "08": "Indústria Extrativa (Minerais Não-Metálicos)",
    "09": "Indústria Extrativa (Atividades de Apoio)",
    # SEÇÃO C: INDÚSTRIAS DE TRANSFORMAÇÃO
    "10": "Indústria (Alimentos)",
    "11": "Indústria (Bebidas)",
    "12": "Indústria (Fumo)",
    "13": "Indústria (Têxteis)",
    "14": "Indústria (Vestuário e Acessórios)",
    "15": "Indústria (Couro e Calçados)",
    "16": "Indústria (Madeira)",
    "17": "Indústria (Celulose e Papel)",
    "18": "Indústria (Impressão e Reprodução)",
    "19": "Indústria (Coque, Petróleo e Biocombustíveis)",
    "20": "Indústria (Químicos)",
    "21": "Indústria (Farmacêuticos)",
    "22": "Indústria (Borracha e Plástico)",
    "23": "Indústria (Minerais Não-Metálicos)",
    "24": "Indústria (Metalurgia)",
    "25": "Indústria (Produtos de Metal)",
    "26": "Indústria (Equipamentos de Informática, Eletrônicos)",
    "27": "Indústria (Máquinas e Equipamentos Elétricos)",
    "28": "Indústria (Máquinas e Equipamentos Mecânicos)",
    "29": "Indústria (Veículos Automotores)",
    "30": "Indústria (Outros Equipamentos de Transporte)",
    "31": "Indústria (Móveis)",
    "32": "Indústria (Produtos Diversos)",
    "33": "Indústria (Manutenção e Reparação)",
    # SEÇÃO D: ELETRICIDADE E GÁS
    "35": "Serviços (Eletricidade, Gás e Utilidades)",  # Pode ser considerado Serviço ou Infraestrutura
    # SEÇÃO E: ÁGUA, ESGOTO, ATIVIDADES DE GESTÃO DE RESÍDUOS E DESCONTAMINAÇÃO
    "36": "Serviços (Água e Esgoto)",
    "37": "Serviços (Esgoto e Atividades Relacionadas)",
    "38": "Serviços (Coleta e Tratamento de Resíduos)",
    "39": "Serviços (Descontaminação e Gestão de Resíduos)",
    # SEÇÃO F: CONSTRUÇÃO
    "41": "Construção (Edifícios)",
    "42": "Construção (Infraestrutura)",
    "43": "Construção (Serviços Especializados)",
    # SEÇÃO G: COMÉRCIO; REPARAÇÃO DE VEÍCULOS AUTOMOTORES E MOTOCICLETAS
    "45": "Comércio/Serviços (Automotivo - Veículos)",
    "46": "Comércio (Atacadista)",
    "47": "Comércio (Varejista)",
    # SEÇÃO H: TRANSPORTE, ARMAZENAGEM E CORREIO
    "49": "Serviços (Transporte Terrestre)",
    "50": "Serviços (Transporte Aquaviário)",
    "51": "Serviços (Transporte Aéreo)",
    "52": "Serviços (Armazenagem e Atividades Auxiliares de Transporte)",
    "53": "Serviços (Correio e Entregas)",
    # SEÇÃO I: ALOJAMENTO E ALIMENTAÇÃO
    "55": "Serviços (Alojamento - Hotéis, etc.)",
    "56": "Serviços (Alimentação - Restaurantes, Bares)",
    # SEÇÃO J: INFORMAÇÃO E COMUNICAÇÃO
    "58": "Serviços (Edição e Edição Integrada à Impressão)",
    "59": "Serviços (Atividades Cinematográficas, Vídeo e TV)",
    "60": "Serviços (Rádio e Televisão)",
    "61": "Serviços (Telecomunicações)",
    "62": "Serviços (Tecnologia da Informação - TI)",
    "63": "Serviços (Serviços de Informação)",
    # SEÇÃO K: ATIVIDADES FINANCEIRAS, DE SEGUROS E SERVIÇOS RELACIONADOS
    "64": "Serviços (Financeiros - Bancos, Holdings)",
    "65": "Serviços (Seguros e Previdência Complementar)",
    "66": "Serviços (Atividades Auxiliares Financeiras e Seguros)",
    # SEÇÃO L: ATIVIDADES IMOBILIÁRIAS
    "68": "Serviços (Atividades Imobiliárias)",
    # SEÇÃO M: ATIVIDADES PROFISSIONAIS, CIENTÍFICAS E TÉCNICAS
    "69": "Serviços (Jurídicos, Contabilidade, Auditoria)",
    "70": "Serviços (Consultoria Empresarial, Sedes de Empresas)",
    "71": "Serviços (Arquitetura, Engenharia, Testes Técnicos)",
    "72": "Serviços (Pesquisa e Desenvolvimento Científico)",
    "73": "Serviços (Publicidade e Pesquisa de Mercado)",
    "74": "Serviços (Profissionais, Científicas e Técnicas Diversas)",
    "75": "Serviços (Atividades Veterinárias)",
    # SEÇÃO N: ATIVIDADES ADMINISTRATIVAS E SERVIÇOS COMPLEMENTARES
    "77": "Serviços (Aluguéis Não-Imobiliários e Gestão de Ativos)",
    "78": "Serviços (Seleção e Agenciamento de Mão-de-Obra)",
    "79": "Serviços (Agências de Viagens e Operadores Turísticos)",
    "80": "Serviços (Segurança e Investigação)",
    "81": "Serviços (Serviços para Edifícios e Paisagismo)",
    "82": "Serviços (Serviços de Escritório e Apoio Administrativo)",
    # SEÇÃO O: ADMINISTRAÇÃO PÚBLICA, DEFESA E SEGURIDADE SOCIAL
    "84": "Administração Pública",  # Geralmente não aplicável a fornecedores, mas incluído
    # SEÇÃO P: EDUCAÇÃO
    "85": "Serviços (Educação)",
    # SEÇÃO Q: SAÚDE HUMANA E SERVIÇOS SOCIAIS
    "86": "Serviços (Saúde)",
    "87": "Serviços (Assistência Social em Residências Coletivas)",
    "88": "Serviços (Assistência Social sem Alojamento)",
    # SEÇÃO R: ARTES, CULTURA, ESPORTE E RECREAÇÃO
    "90": "Serviços (Artes, Cultura, Espetáculos)",
    "91": "Serviços (Museus, Bibliotecas, Arquivos)",
    "92": "Serviços (Jogos de Azar e Apostas)",
    "93": "Serviços (Esportes e Recreação)",
    # SEÇÃO S: OUTRAS ATIVIDADES DE SERVIÇOS
    "94": "Serviços (Atividades de Organizações Associativas)",
    "95": "Serviços (Reparação de Computadores e Objetos)",
    "96": "Serviços (Serviços Pessoais Diversos)",
    # SEÇÃO T: SERVIÇOS DOMÉSTICOS
    "97": "Serviços (Serviços Domésticos)",
    # SEÇÃO U: ORGANISMOS INTERNACIONAIS E OUTRAS INSTITUIÇÕES EXTRATERRITORIAIS
    "99": "Organismos Internacionais",
}


def get_ramo_from_cnae(cnae_code: str | None) -> str | None:
    """Busca o ramo de atividade no mapa usando os 2 primeiros dígitos do CNAE."""
    if not cnae_code:
        return None

    # Garante que o código tem pelo menos 2 dígitos
    cnae_code = str(cnae_code).strip()
    if len(cnae_code) < 2:
        return None

    prefixo = cnae_code[:2]
    return CNAE_TO_RAMO_MAP.get(prefixo, "Ramo Desconhecido ou Não Mapeado")


# ==========================================================
# CFOPs Representativos por Ramo de Atividade (Foco Compra/Venda)
# ==========================================================

# --- Agronegócio (CNAE 01-03) ---
AGRO_CFOP_ENTRADA = [
    "1101",
    "2101",  # Compra para Industrialização ou Produção Rural
    "1102",
    "2102",  # Compra para Comercialização
    "1556",
    "2556",  # Compra de Material para Uso ou Consumo
    "1551",
    "2551",  # Compra de Bem para o Ativo Imobilizado
]
AGRO_CFOP_SAIDA = [
    "5101",
    "6101",  # Venda de Produção do Estabelecimento (Rural)
    "5102",
    "6102",  # Venda de Mercadoria Adquirida ou Recebida de Terceiros
]

# --- Indústria Extrativa (CNAE 05-09) ---
EXTRATIVA_CFOP_ENTRADA = [
    "1101",
    "2101",  # Compra para Industrialização
    "1556",
    "2556",  # Compra de Material para Uso ou Consumo
    "1551",
    "2551",  # Compra de Bem para o Ativo Imobilizado
]
EXTRATIVA_CFOP_SAIDA = [
    "5101",
    "6101",  # Venda de Produção do Estabelecimento (Industrial)
]

# --- Indústria de Transformação (CNAE 10-33) ---
INDUSTRIA_CFOP_ENTRADA = [
    "1101",
    "2101",  # Compra para Industrialização ou Produção Rural
    "1124",
    "2124",  # Industrialização Efetuada por Outra Empresa
    "1556",
    "2556",  # Compra de Material para Uso ou Consumo
    "1551",
    "2551",  # Compra de Bem para o Ativo Imobilizado
]
INDUSTRIA_CFOP_SAIDA = [
    "5101",
    "6101",  # Venda de Produção do Estabelecimento (Industrial)
    "5124",
    "6124",  # Industrialização Efetuada para Outra Empresa
    "5901",
    "6901",  # Remessa para Industrialização por Encomenda
    "5902",
    "6902",  # Retorno de Mercadoria Utilizada na Industrialização por Encomenda
]

# --- Construção (CNAE 41-43) ---
CONSTRUCAO_CFOP_ENTRADA = [
    "1126",
    "2126",  # Compra para Utilização na Prestação de Serviço Sujeita ao ICMS
    "1556",
    "2556",  # Compra de Material para Uso ou Consumo
    "1551",
    "2551",  # Compra de Bem para o Ativo Imobilizado
]
CONSTRUCAO_CFOP_SAIDA = [
    "5122",
    "6122",  # Venda de Produção do Estabelecimento Remetida para Industrialização (pode ocorrer)
    # Principalmente CFOPs de Serviço, se NF-e conjugada, ou códigos municipais (NFS-e)
    "5933",
    "6933",  # Prestação de Serviço Tributado pelo ISSQN (quando NF-e conjugada)
]

# --- Comércio Atacadista e Varejista (CNAE 45-47) ---
COMERCIO_CFOP_ENTRADA = [
    "1102",
    "2102",  # Compra para Comercialização
    "1403",
    "2403",  # Compra para Comercialização em Operação com Mercadoria Sujeita a ST
    "1556",
    "2556",  # Compra de Material para Uso ou Consumo
    "1551",
    "2551",  # Compra de Bem para o Ativo Imobilizado
]
COMERCIO_CFOP_SAIDA = [
    "5102",
    "6102",  # Venda de Mercadoria Adquirida ou Recebida de Terceiros
    "5405",
    "6405",  # Venda de Mercadoria Adquirida ou Recebida Sujeita a ST, na Condição de Contribuinte Substituto
    # CFOPs de Venda ao Consumidor Final:
    "5102",
    "6102",  # (Para não contribuintes)
    "5103",
    "6103",
    "5104",
    "6104",  # Venda produção estabelecimento para ZFM ou ALC
    "5109",
    "6109",  # Venda produção estabelecimento, destinada à ZFM ou ALC
    # ... e muitos outros dependendo do regime e destino
]

# --- Transporte (CNAE 49-53) ---
TRANSPORTE_CFOP_ENTRADA = [  # Entradas são menos comuns como CFOP principal
    "1351",
    "2351",  # Aquisição de Serviço de Transporte para Execução de Serviço da Mesma Natureza
    "1352",
    "2352",  # Aquisição de Serviço de Transporte por Estabelecimento Industrial
    "1353",
    "2353",  # Aquisição de Serviço de Transporte por Estabelecimento Comercial
    # ... outros dependendo de quem contrata
]
TRANSPORTE_CFOP_SAIDA = [
    "5351",
    "6351",  # Prestação de Serviço de Transporte para Execução de Serviço da Mesma Natureza
    "5352",
    "6352",  # Prestação de Serviço de Transporte a Estabelecimento Industrial
    "5353",
    "6353",  # Prestação de Serviço de Transporte a Estabelecimento Comercial
    "5357",
    "6357",  # Prestação de Serviço de Transporte a Não Contribuinte
    # ... e muitos outros (coleta, redespacho, multimodal)
]

# --- Serviços Gerais (Quando Faturados via NF-e, ex: conjugada) ---
# (Muitos serviços CNAE J, M, N, P, Q, R, S usam NFS-e municipal)
SERVICOS_NFE_CFOP_SAIDA = [
    "5933",
    "6933",  # Prestação de Serviço Tributado pelo ISSQN
    "5102",
    "6102",  # Às vezes usado para "Venda" de serviço se envolver mercadoria
]
SERVICOS_NFE_CFOP_ENTRADA = [  # Menos comum, depende de quem contrata
    "1126",
    "2126",  # Compra para Utilização na Prestação de Serviço Sujeita ao ICMS
    "1933",
    "2933",  # Aquisição de Serviço Tributado pelo ISSQN
]


# ==========================================================
# NCMs Representativos por Ramo de Atividade (Foco nos Capítulos)
# ==========================================================
AGRO_NCM_CAPITULOS = list(range(1, 25))  # Capítulos 01 a 24

# --- Indústria Extrativa (CNAE 05-09) ---
# Combustíveis minerais, óleos minerais; Minérios, escórias e cinzas, etc.
EXTRATIVA_NCM_CAPITULOS = [25, 26, 27]

# --- Indústria de Transformação (CNAE 10-33) ---
# Muito amplo, cobre quase tudo que é manufaturado. Exemplos:
INDUSTRIA_NCM_CAPITULOS_EXEMPLOS = [
    28,
    29,
    30,
    31,
    32,
    33,
    34,
    35,
    36,
    37,
    38,
    # Plásticos/Borracha (39-40)
    39,
    40,
    # Têxteis/Vestuário/Couro/Calçados (50-67)
    50,
    51,
    52,
    53,
    54,
    55,
    56,
    57,
    58,
    59,
    60,
    61,
    62,
    63,
    64,
    65,
    66,
    67,
    # Metais (72-83)
    72,
    73,
    74,
    75,
    76,
    78,
    79,
    80,
    81,
    82,
    83,
    # Máquinas/Equipamentos (84-85)
    84,
    85,
    # Veículos/Transporte (86-89)
    86,
    87,
    88,
    89,
    # Outros (Móveis, Instrumentos, Diversos)
    94,  # Móveis
    90,  # Instrumentos Ópticos, etc.
]

# --- Construção (CNAE 41-43) ---
# Materiais de construção são diversos, NCMs da Indústria se aplicam. Ex:
# Cimento (25), Cerâmica (69), Vidro (70), Ferro/Aço (72, 73), Madeira (44)
CONSTRUCAO_NCM_CAPITULOS_EXEMPLOS = [
    25,
    68,
    69,
    70,
    72,
    73,
    44,
    39,
] 

# --- Comércio Atacadista e Varejista (CNAE 45-47) ---
# O Comércio lida com produtos de TODOS os setores.
# Exemplos comuns no varejo:
COMERCIO_NCM_CAPITULOS_EXEMPLOS = [
    61,
    62,
    63,  # Vestuário e acessórios
    85,  # Eletrônicos
    94,  # Móveis
    33,  # Cosméticos
]
# Exemplo Específico para Automotivo (peças)
AUTO_NCM_PECAS_CAPITULOS = [
    84,
    85,
    87,
    40,
    70,
    73,
    45
]  # Motores, Elétricos, Veículos, Borracha, Vidro, Ferro/Aço

# --- Serviços Gerais ---
# NCM geralmente não aplicável ou usa-se código genérico "00000000".
# Para serviços específicos que podem estar na NF-e (ex: software), NCMs como:
SERVICOS_NCM_EXEMPLOS = [
    "85234990",  # Mídias gravadas (pode incluir software)
]


def format_chapters(chapters):
    return [f"{ch:02d}" for ch in chapters]


# FUNÇÕES DE AÇÃO CUSTOMIZADA 
def custom_action_agronegocio(data: dict) -> dict:
    """Realiza verificações específicas para o Agronegócio."""
    results = {"warnings": [], "info": []}
    cfop = data.get("cfop")
    ncm_value = data.get("ncm")
    ncm = str(ncm_value).strip() if ncm_value is not None else ""

    # Monitoramento CFOP
    if cfop in AGRO_CFOP_SAIDA:
        results["info"].append(
            f"Monitoramento CFOP: {cfop} indica Venda de Produção/Mercadoria Agrícola."
        )
    elif cfop in AGRO_CFOP_ENTRADA:
        results["info"].append(
            f"Monitoramento CFOP: {cfop} indica Compra (Insumos, Consumo, Ativo) no Agronegócio."
        )
    else:
        results["warnings"].append(
            f"CFOP {cfop} não mapeado como operação primária do Agronegócio (Verificar)."
        )

    # Verificação NCM (Capítulo)
    if ncm[:2] in AGRO_NCM_CAPITULOS:
        results["info"].append(
            f"Validação NCM: {ncm} pertence a capítulos comuns do Agronegócio."
        )
    else:
        results["warnings"].append(
            f"Validação NCM: {ncm} NÃO pertence a capítulos comuns do Agronegócio (Verificar)."
        )

    # Placeholder Impostos
    results["info"].append(
        "Placeholder: Lógica de cálculo de impostos específicos do agro (Ex: FUNRURAL) a ser implementada."
    )
    return results


def custom_action_automotivo(data: dict) -> dict:
    """Realiza verificações específicas para o Setor Automotivo."""
    results = {"warnings": [], "info": []}

    # --- GARANTIR QUE NCM É STRING ---
    ncm_value = data.get("ncm")
    ncm = str(ncm_value).strip() if ncm_value is not None else ""
    print(f"ncm_value {ncm_value}, ncm {ncm}")
    # --- FIM DA GARANTIA ---

    cfop = data.get("cfop")
    descricao = data.get("descricao_item", "").lower()

    # Validação NCM (Capítulo)
    # Agora 'ncm' é garantidamente uma string, então startswith funcionará.
    if ncm and any(ncm.startswith(prefix) for prefix in AUTO_NCM_PECAS_CAPITULOS):
        results["info"].append(
            f"Validação NCM: {ncm} pertence a capítulos comuns de peças/componentes automotivos."
        )
    elif ncm:
        results["warnings"].append(
            f"Validação NCM: {ncm} não usual para peças automotivas (Verificar)."
        )
    else:
        results["warnings"].append(
            "Validação NCM: Código NCM não encontrado ou inválido no XML."
        )

    # Validação Descrição (Keywords)
    keywords_pecas = [
        "filtro",
        "oleo",
        "motor",
        "vela",
        "pneu",
        "freio",
        "pastilha",
        "amortecedor",
        "correia",
    ]
    if any(keyword in descricao for keyword in keywords_pecas):
        results["info"].append(
            "Validação Descrição: Item parece ser peça/componente automotivo."
        )

    # Monitoramento CFOP (Comércio/Serviço)
    if cfop in COMERCIO_CFOP_SAIDA:
        results["info"].append(
            f"Monitoramento CFOP: {cfop} indica operação de Venda (Comércio)."
        )
    elif cfop in COMERCIO_CFOP_ENTRADA:
        results["info"].append(
            f"Monitoramento CFOP: {cfop} indica operação de Compra (Comércio)."
        )
    elif cfop in SERVICOS_NFE_CFOP_SAIDA or cfop in SERVICOS_NFE_CFOP_ENTRADA:
        results["info"].append(
            f"Monitoramento CFOP: {cfop} indica operação de Serviço (Reparação)."
        )
    else:
        results["warnings"].append(
            f"CFOP {cfop} não mapeado como operação primária do Comércio/Serviço Automotivo (Verificar)."
        )

    # Placeholders Validações Complexas
    results["info"].append(
        "Placeholder: Conferência detalhada de códigos de peças e compatibilidade requer integração externa/base de dados."
    )
    return results


def custom_action_industria(data: dict) -> dict:
    """Realiza verificações específicas para a Indústria (Transformação)."""
    results = {"warnings": [], "info": []}
    valor_ipi = data.get(
        "valor_ipi"
    )  # Não definir default 0, para saber se veio ou não
    cfop = data.get("cfop")
    ncm_value = data.get("ncm")
    ncm = str(ncm_value).strip() if ncm_value is not None else ""
    # Apuração IPI
    if valor_ipi is not None and valor_ipi > 0:
        results["info"].append(
            f"Apuração IPI: Valor do IPI R$ {valor_ipi:.2f} identificado na nota."
        )
    elif valor_ipi == 0:
        results["info"].append("Apuração IPI: Valor do IPI é zero.")
    else:  # valor_ipi é None
        results["info"].append(
            "Apuração IPI: Campo IPI não encontrado ou não preenchido na nota."
        )

    # Monitoramento CFOP (Indústria)
    if cfop in INDUSTRIA_CFOP_SAIDA:
        results["info"].append(
            f"Monitoramento CFOP: {cfop} indica operação de Saída Industrial."
        )
    elif cfop in INDUSTRIA_CFOP_ENTRADA:
        results["info"].append(
            f"Monitoramento CFOP: {cfop} indica operação de Entrada Industrial."
        )
    else:
        results["warnings"].append(
            f"CFOP {cfop} não mapeado como operação primária da Indústria (Verificar)."
        )

    # Verificação NCM (Ampla para Indústria)
    if any(ncm.startswith(f"{i:02d}") for i in range(28, 97)):  # Intervalo amplo
        results["info"].append(
            f"Validação NCM: {ncm} pertence a capítulos comuns da Indústria de Transformação."
        )

    # Placeholders ST e Custos
    results["info"].append(
        "Placeholder: Lógica de apuração de Substituição Tributária (ST) a ser implementada (depende de NCM, UF, regime)."
    )
    results["info"].append(
        "Placeholder: Geração de insumos para cálculo de custos de produção requer integração com sistema de custeio."
    )
    return results


# --- Funções Adicionais para Outros Ramos ---

def custom_action_comercio(data: dict) -> dict:
    """Realiza verificações específicas para Comércio (Atacado/Varejo)."""
    results = {"warnings": [], "info": []}
    cfop = data.get("cfop")
    if cfop in COMERCIO_CFOP_SAIDA:
        results["info"].append(
            f"Monitoramento CFOP: {cfop} indica operação de Venda (Comércio)."
        )
    elif cfop in COMERCIO_CFOP_ENTRADA:
        results["info"].append(
            f"Monitoramento CFOP: {cfop} indica operação de Compra (Comércio)."
        )
    else:
        results["warnings"].append(
            f"CFOP {cfop} não mapeado como operação primária do Comércio (Verificar)."
        )

    results["info"].append(
        "Placeholder: Lógica de apuração de Substituição Tributária (ST) a ser implementada."
    )
    return results


def custom_action_servicos(data: dict) -> dict:
    """Realiza verificações genéricas para Serviços (quando NF-e)."""
    results = {"warnings": [], "info": []}
    cfop = data.get("cfop")
    ncm_value = data.get("ncm")
    ncm = str(ncm_value).strip() if ncm_value is not None else ""

    if cfop in SERVICOS_NFE_CFOP_SAIDA:
        results["info"].append(
            f"Monitoramento CFOP: {cfop} indica operação de Prestação de Serviço (NF-e)."
        )
    elif cfop in SERVICOS_NFE_CFOP_ENTRADA:
        results["info"].append(
            f"Monitoramento CFOP: {cfop} indica operação de Aquisição de Serviço (NF-e)."
        )
    else:
        results["warnings"].append(
            f"CFOP {cfop} não mapeado como operação de Serviço comum em NF-e (Verificar)."
        )

    if ncm is None or ncm == "00000000":
        results["info"].append(
            "Validação NCM: Ausente ou genérico (00000000), comum para serviços."
        )
    else:
        results["info"].append(
            f"Validação NCM: {ncm} presente, verificar se corresponde a material usado no serviço."
        )

    results["info"].append(
        "Observação: Muitas operações de serviço usam NFS-e municipal com códigos de serviço específicos."
    )
    return results


def custom_action_construcao(data: dict) -> dict:
    """Realiza verificações específicas para Construção."""
    results = {"warnings": [], "info": []}
    cfop = data.get("cfop")
    ncm_value = data.get("ncm")
    ncm = str(ncm_value).strip() if ncm_value is not None else ""

    # Monitoramento CFOP (Construção)
    if cfop in CONSTRUCAO_CFOP_ENTRADA:
        results["info"].append(
            f"Monitoramento CFOP: {cfop} indica Compra de Material/Ativo para Construção/Serviço."
        )
    elif cfop in CONSTRUCAO_CFOP_SAIDA:
        results["info"].append(
            f"Monitoramento CFOP: {cfop} indica Saída (Venda ou Serviço) relacionada à Construção."
        )
    else:
        results["warnings"].append(
            f"CFOP {cfop} não mapeado como operação primária da Construção (Verificar)."
        )

    # Verificação NCM (Materiais Comuns)
    if any(ncm.startswith(prefix) for prefix in CONSTRUCAO_NCM_CAPITULOS_EXEMPLOS):
        results["info"].append(
            f"Validação NCM: {ncm} pertence a capítulos comuns de materiais de construção."
        )

    results["info"].append(
        "Placeholder: Lógica para impostos específicos da construção (Ex: INSS sobre Mão de Obra) a ser implementada."
    )
    return results


def custom_action_transporte(data: dict) -> dict:
    """Realiza verificações específicas para Transporte."""
    results = {"warnings": [], "info": []}
    cfop = data.get("cfop")

    # Monitoramento CFOP (Transporte)
    if cfop in TRANSPORTE_CFOP_SAIDA:
        results["info"].append(
            f"Monitoramento CFOP: {cfop} indica Prestação de Serviço de Transporte."
        )
    elif cfop in TRANSPORTE_CFOP_ENTRADA:
        results["info"].append(
            f"Monitoramento CFOP: {cfop} indica Aquisição de Serviço de Transporte."
        )
    else:
        results["warnings"].append(
            f"CFOP {cfop} não mapeado como operação de Transporte (Verificar CT-e)."
        )

    results["info"].append(
        "Observação: Detalhes do transporte (origem, destino, frete) geralmente estão no CT-e (Conhecimento de Transporte Eletrônico)."
    )
    return results

def custom_action_servicos_utilidades(data: dict) -> dict:
    return custom_action_servicos(data)


def custom_action_alojamento_alimentacao(data: dict) -> dict:
    return custom_action_servicos(data)


def custom_action_ti_comunicacao(data: dict) -> dict:
    return custom_action_servicos(data)


def custom_action_financeiro(data: dict) -> dict:
    return {
        "warnings": [],
        "info": ["Ação customizada para Financeiro não implementada."],
    }


def custom_action_imobiliario(data: dict) -> dict:
    return {
        "warnings": [],
        "info": ["Ação customizada para Imobiliário não implementada."],
    }


def custom_action_servicos_profissionais(data: dict) -> dict:
    return {
        "warnings": [],
        "info": ["Ação customizada para Serv. Profissionais não implementada."],
    }


def custom_action_servicos_administrativos(data: dict) -> dict:
    return {
        "warnings": [],
        "info": ["Ação customizada para Serv. Administrativos não implementada."],
    }


def custom_action_educacao(data: dict) -> dict:
    return {
        "warnings": [],
        "info": ["Ação customizada para Educação não implementada."],
    }


def custom_action_saude(data: dict) -> dict:
    return {"warnings": [], "info": ["Ação customizada para Saúde não implementada."]}


def custom_action_artes_cultura(data: dict) -> dict:
    return {
        "warnings": [],
        "info": ["Ação customizada para Artes/Cultura não implementada."],
    }


def custom_action_outros_servicos(data: dict) -> dict:
    return {
        "warnings": [],
        "info": ["Ação customizada para Outros Serviços não implementada."],
    }


RAMO_ACTION_MAP = {
    # SEÇÃO A: AGRICULTURA, PECUÁRIA, PRODUÇÃO FLORESTAL, PESCA E AQÜICULTURA
    "Agronegócio (Agricultura, Pecuária)": custom_action_agronegocio,
    "Agronegócio (Produção Florestal)": custom_action_agronegocio,
    "Agronegócio (Pesca e Aquicultura)": custom_action_agronegocio,
    # SEÇÃO B: INDÚSTRIAS EXTRATIVAS (Pode ter regras próprias ou usar as da Indústria)
    "Indústria Extrativa (Carvão Mineral)": custom_action_industria,  # Ou custom_action_industria_extrativa
    "Indústria Extrativa (Petróleo e Gás)": custom_action_industria,  # Ou custom_action_industria_extrativa
    "Indústria Extrativa (Minerais Metálicos)": custom_action_industria,  # Ou custom_action_industria_extrativa
    "Indústria Extrativa (Minerais Não-Metálicos)": custom_action_industria,  # Ou custom_action_industria_extrativa
    "Indústria Extrativa (Atividades de Apoio)": custom_action_industria,  # Ou custom_action_industria_extrativa
    # SEÇÃO C: INDÚSTRIAS DE TRANSFORMAÇÃO
    "Indústria (Alimentos)": custom_action_industria,
    "Indústria (Bebidas)": custom_action_industria,
    "Indústria (Fumo)": custom_action_industria,
    "Indústria (Têxteis)": custom_action_industria,
    "Indústria (Vestuário e Acessórios)": custom_action_industria,
    "Indústria (Couro e Calçados)": custom_action_industria,
    "Indústria (Madeira)": custom_action_industria,
    "Indústria (Celulose e Papel)": custom_action_industria,
    "Indústria (Impressão e Reprodução)": custom_action_industria,
    "Indústria (Coque, Petróleo e Biocombustíveis)": custom_action_industria,
    "Indústria (Químicos)": custom_action_industria,
    "Indústria (Farmacêuticos)": custom_action_industria,
    "Indústria (Borracha e Plástico)": custom_action_industria,
    "Indústria (Minerais Não-Metálicos)": custom_action_industria,
    "Indústria (Metalurgia)": custom_action_industria,
    "Indústria (Produtos de Metal)": custom_action_industria,
    "Indústria (Equipamentos de Informática, Eletrônicos)": custom_action_industria,
    "Indústria (Máquinas e Equipamentos Elétricos)": custom_action_industria,
    "Indústria (Máquinas e Equipamentos Mecânicos)": custom_action_industria,
    "Indústria (Veículos Automotores)": custom_action_industria,  # Pode ter regras específicas, mas a base é industrial
    "Indústria (Outros Equipamentos de Transporte)": custom_action_industria,
    "Indústria (Móveis)": custom_action_industria,
    "Indústria (Produtos Diversos)": custom_action_industria,
    "Indústria (Manutenção e Reparação)": custom_action_industria,  # Manutenção industrial
    # SEÇÃO D: ELETRICIDADE E GÁS (Pode ser considerado Serviço ou ter regras próprias)
    "Serviços (Eletricidade, Gás e Utilidades)": custom_action_servicos,  # Ou custom_action_servicos_utilidades
    # SEÇÃO E: ÁGUA, ESGOTO, RESÍDUOS (Pode ser considerado Serviço)
    "Serviços (Água e Esgoto)": custom_action_servicos,
    "Serviços (Esgoto e Atividades Relacionadas)": custom_action_servicos,
    "Serviços (Coleta e Tratamento de Resíduos)": custom_action_servicos,
    "Serviços (Descontaminação e Gestão de Resíduos)": custom_action_servicos,
    # SEÇÃO F: CONSTRUÇÃO
    "Construção (Edifícios)": custom_action_construcao,
    "Construção (Infraestrutura)": custom_action_construcao,
    "Construção (Serviços Especializados)": custom_action_construcao,  # Ou custom_action_servicos
    # SEÇÃO G: COMÉRCIO; REPARAÇÃO DE VEÍCULOS AUTOMOTORES E MOTOCICLETAS
    "Comércio/Serviços (Automotivo - Veículos)": custom_action_automotivo,  # Função específica já criada
    "Comércio (Atacadista)": custom_action_comercio,
    "Comércio (Varejista)": custom_action_comercio,
    # SEÇÃO H: TRANSPORTE, ARMAZENAGEM E CORREIO
    "Serviços (Transporte Terrestre)": custom_action_transporte,
    "Serviços (Transporte Aquaviário)": custom_action_transporte,
    "Serviços (Transporte Aéreo)": custom_action_transporte,
    "Serviços (Armazenagem e Atividades Auxiliares de Transporte)": custom_action_transporte,  # Ou custom_action_servicos
    "Serviços (Correio e Entregas)": custom_action_transporte,  # Ou custom_action_servicos
    # SEÇÃO I: ALOJAMENTO E ALIMENTAÇÃO
    "Serviços (Alojamento - Hotéis, etc.)": custom_action_servicos,  # Ou custom_action_alojamento_alimentacao
    "Serviços (Alimentação - Restaurantes, Bares)": custom_action_servicos,  # Ou custom_action_alojamento_alimentacao
    # SEÇÃO J: INFORMAÇÃO E COMUNICAÇÃO
    "Serviços (Edição e Edição Integrada à Impressão)": custom_action_servicos,
    "Serviços (Atividades Cinematográficas, Vídeo e TV)": custom_action_servicos,
    "Serviços (Rádio e Televisão)": custom_action_servicos,
    "Serviços (Telecomunicações)": custom_action_servicos,  # Ou custom_action_ti_comunicacao
    "Serviços (Tecnologia da Informação - TI)": custom_action_servicos,  # Ou custom_action_ti_comunicacao
    "Serviços (Serviços de Informação)": custom_action_servicos,  # Ou custom_action_ti_comunicacao
    # SEÇÃO K: ATIVIDADES FINANCEIRAS, DE SEGUROS E SERVIÇOS RELACIONADOS
    "Serviços (Financeiros - Bancos, Holdings)": custom_action_financeiro,
    "Serviços (Seguros e Previdência Complementar)": custom_action_financeiro,
    "Serviços (Atividades Auxiliares Financeiras e Seguros)": custom_action_financeiro,
    # SEÇÃO L: ATIVIDADES IMOBILIÁRIAS
    "Serviços (Atividades Imobiliárias)": custom_action_imobiliario,  # Ou custom_action_servicos
    # SEÇÃO M: ATIVIDADES PROFISSIONAIS, CIENTÍFICAS E TÉCNICAS
    "Serviços (Jurídicos, Contabilidade, Auditoria)": custom_action_servicos_profissionais,
    "Serviços (Consultoria Empresarial, Sedes de Empresas)": custom_action_servicos_profissionais,
    "Serviços (Arquitetura, Engenharia, Testes Técnicos)": custom_action_servicos_profissionais,
    "Serviços (Pesquisa e Desenvolvimento Científico)": custom_action_servicos_profissionais,
    "Serviços (Publicidade e Pesquisa de Mercado)": custom_action_servicos_profissionais,  # Ou custom_action_marketing
    "Serviços (Profissionais, Científicas e Técnicas Diversas)": custom_action_servicos_profissionais,
    "Serviços (Atividades Veterinárias)": custom_action_saude,  # Ou custom_action_servicos
    # SEÇÃO N: ATIVIDADES ADMINISTRATIVAS E SERVIÇOS COMPLEMENTARES
    "Serviços (Aluguéis Não-Imobiliários e Gestão de Ativos)": custom_action_servicos_administrativos,
    "Serviços (Seleção e Agenciamento de Mão-de-Obra)": custom_action_servicos_administrativos,  # Ou custom_action_rh
    "Serviços (Agências de Viagens e Operadores Turísticos)": custom_action_servicos_administrativos,
    "Serviços (Segurança e Investigação)": custom_action_servicos_administrativos,
    "Serviços (Serviços para Edifícios e Paisagismo)": custom_action_servicos_administrativos,
    "Serviços (Serviços de Escritório e Apoio Administrativo)": custom_action_servicos_administrativos,
    # SEÇÃO O: ADMINISTRAÇÃO PÚBLICA, DEFESA E SEGURIDADE SOCIAL (Raramente será o Ramo do Fornecedor)
    "Administração Pública": None,  # Ou uma função genérica, se aplicável
    # SEÇÃO P: EDUCAÇÃO
    "Serviços (Educação)": custom_action_educacao,  # Ou custom_action_servicos
    # SEÇÃO Q: SAÚDE HUMANA E SERVIÇOS SOCIAIS
    "Serviços (Saúde)": custom_action_saude,
    "Serviços (Assistência Social em Residências Coletivas)": custom_action_saude,  # Ou custom_action_servicos_sociais
    "Serviços (Assistência Social sem Alojamento)": custom_action_saude,  # Ou custom_action_servicos_sociais
    # SEÇÃO R: ARTES, CULTURA, ESPORTE E RECREAÇÃO
    "Serviços (Artes, Cultura, Espetáculos)": custom_action_artes_cultura,  # Ou custom_action_servicos
    "Serviços (Museus, Bibliotecas, Arquivos)": custom_action_artes_cultura,  # Ou custom_action_servicos
    "Serviços (Jogos de Azar e Apostas)": custom_action_outros_servicos,  # Ou custom_action_servicos
    "Serviços (Esportes e Recreação)": custom_action_artes_cultura,  # Ou custom_action_servicos
    # SEÇÃO S: OUTRAS ATIVIDADES DE SERVIÇOS
    "Serviços (Atividades de Organizações Associativas)": custom_action_outros_servicos,
    "Serviços (Reparação de Computadores e Objetos)": custom_action_outros_servicos,  # Pode ser TI ou Indústria(Manutenção)
    "Serviços (Serviços Pessoais Diversos)": custom_action_outros_servicos,
    # SEÇÃO T: SERVIÇOS DOMÉSTICOS (Raramente aplicável a NF-e)
    "Serviços (Serviços Domésticos)": None,  # Ou custom_action_outros_servicos
    # SEÇÃO U: ORGANISMOS INTERNACIONAIS (Raramente aplicável a NF-e)
    "Organismos Internacionais": None,
    # Ramo Padrão/Desconhecido
    "Ramo Desconhecido ou Não Mapeado": None,  # Nenhuma ação específica
}


def execute_custom_action(ramo: str | None, data: dict) -> dict | None:
    """
    Executa a ação customizada com base no ramo de atividade detectado.
    """
    if not ramo or ramo not in RAMO_ACTION_MAP:
        print(f"Nenhuma ação customizada definida para o ramo: {ramo}")
        return None

    action_function = RAMO_ACTION_MAP[ramo]
    print(f"Executando ação customizada para: {ramo}")
    return action_function(data)
