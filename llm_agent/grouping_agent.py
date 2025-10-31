from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from config.settings import settings


class GroupingOutput(BaseModel):
    """Define a estrutura de saída para o agrupamento da IA."""

    tipo_documento: str = Field(
        description="Tipo do documento fiscal: Compra, Venda ou Serviço."
    )
    centro_custo: str = Field(
        description="Centro de custo provável (ex: TI, RH, Infraestrutura, Gabinete)."
    )
    natureza_despesa: str = Field(
        description="Natureza da despesa (ex: Material de Consumo, Serviço de Terceiros, Despesa Operacional)."
    )
    finalidade: str = Field(
        description="Finalidade institucional resumida da compra/serviço."
    )
    observacao: str = Field(
        description="Comentários ou observações adicionais relevantes à classificação."
    )


BASE_PROMPT_TEMPLATE = """
**Persona:** Você é um agente de IA especialista em auditoria e gestão orçamentária, atuando nos setores público e privado no Brasil. Sua precisão é crucial.

**Tarefa:** Analisar a descrição de um item/serviço de uma nota fiscal E o ramo de atividade do fornecedor para classificar a despesa de forma estruturada.

**Informações de Entrada:**
1.  **Ramo de Atividade do Fornecedor:** {ramo_atividade} (Use esta informação como CONTEXTO principal para a natureza da despesa. Se for "Não informado", baseie-se apenas na descrição).
2.  **Descrição do Item/Serviço:** {descricao_item}

**Instruções Detalhadas:**
1.  Baseie sua análise **estritamente** nas DUAS informações de entrada fornecidas (descrição e ramo). Não adicione informações externas.
2.  **Use o Ramo de Atividade** para refinar a classificação. Por exemplo, "Consultoria" vindo de uma empresa de "Tecnologia da Informação" provavelmente se refere a serviços de TI, enquanto vindo de "Recursos Humanos" pode ser sobre treinamento.
3.  **Determine as seguintes categorias**, usando terminologia comum da administração pública E considerando as particularidades do ramo informado:
    * **Centro de Custo:** Identifique o departamento interno MAIS PROVÁVEL a ser responsável pela despesa (ex: TI, RH, Manutenção Predial, Marketing, Produção, Administrativo, Gabinete).
    * **Natureza da Despesa:** Forneça a classificação contábil/orçamentária mais adequada, considerando o ramo (ex: Material de Consumo, Material Permanente, Serviço de Terceiros - Pessoa Jurídica, Despesa Operacional, Insumos Agrícolas, Peças Automotivas, Matéria-Prima Industrial).
    * **Finalidade Institucional:** Descreva de forma concisa o propósito principal da aquisição/serviço para a entidade (ex: Manutenção Operacional, Implementação de Sistema, Atividade Fim da Instituição, Insumo para Produção).
4.  Se a descrição for muito vaga ou o ramo não ajudar, use classificações mais genéricas, mas sempre preencha os campos.
5.  Formate sua resposta **EXATAMENTE** conforme as instruções Pydantic abaixo. Não inclua nenhuma explicação adicional fora da estrutura solicitada.

**Análise:**
Ramo de Atividade: {ramo_atividade}
Descrição: {descricao_item}

{format_instructions}
"""

RAMO_REGRAS = {
    "Agronegócio": "Considere CFOPs agrícolas, venda de produtos agropecuários e impostos específicos (FUNRURAL, ICMS-ST).",
    "Automotivo": "Priorize validação de peças, serviços automotivos e compatibilidade de códigos.",
    "Indústria": "Considere IPI, Substituição Tributária e itens de produção industrial.",
    "Setor Público": "Considere regras orçamentárias, centros de custo administrativos e finalidades institucionais.",
    "Comércio": "Classifique produtos de revenda e despesas operacionais típicas do varejo.",
}


def get_grouping_agent(ramo_atividade: str):
    """Cria o agente de IA com prompt ajustado por ramo de atividade."""
    llm = ChatOpenAI(
        model="gpt-3.5-turbo", api_key=settings.OPENAI_API_KEY, temperature=0
    )

    parser = PydanticOutputParser(pydantic_object=GroupingOutput)

    ramo_instrucao = RAMO_REGRAS.get(ramo_atividade, "")
    prompt_text = (
        BASE_PROMPT_TEMPLATE + "\n\nInstruções específicas do ramo:\n" + ramo_instrucao
    )

    prompt = ChatPromptTemplate.from_template(
        prompt_text,
        partial_variables={"format_instructions": parser.get_format_instructions()},
    )

    chain = prompt | llm | parser
    return chain


def group_expense(descricao_item: str, ramo_atividade: str) -> GroupingOutput:
    """Executa o agente de IA para classificar uma despesa."""
    print(f"\n🔎 Iniciando análise de IA para: '{descricao_item}' ({ramo_atividade})")

    try:
        agent = get_grouping_agent(ramo_atividade)
        print(f"-------{agent}")
        result = agent.invoke(
            {"descricao_item": descricao_item, "ramo_atividade": ramo_atividade}
        )

        if isinstance(result, GroupingOutput):
            return result
        elif isinstance(result, dict):
            return GroupingOutput(**result)
        else:
            print(f"⚠️ Retorno inesperado do agente: {type(result)} -> {result}")
            return GroupingOutput(
                tipo_documento="Indefinido",
                centro_custo="Indefinido",
                natureza_despesa="Indefinido",
                finalidade="Indefinido",
                observacao=f"Retorno inválido do agente: {result}",
            )
    except Exception as e:
        print(f"⚠️ Erro ao contatar o agente de IA: {e}")
        return GroupingOutput(
            tipo_documento="Erro",
            centro_custo="Erro",
            natureza_despesa="Erro",
            finalidade="Erro",
            observacao=str(e),
        )
