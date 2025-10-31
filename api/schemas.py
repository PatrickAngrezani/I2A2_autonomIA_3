from pydantic import BaseModel
from typing import Optional, List


class InvoiceInput(BaseModel):
    xml_content: str


class ClassificationOutput(BaseModel):
    categoria_predita: str
    confianca: float


class AnomalyOutput(BaseModel):
    eh_anomalia: bool
    score_anomalia: float


class GroupingOutput(BaseModel):
    centro_custo: str
    natureza_despesa: str
    finalidade: str

class AnalysisResponse(BaseModel):
    dados_extraidos: dict
    classificacao: Optional[ClassificationOutput] = None
    anomalia: Optional[AnomalyOutput] = None
    agrupamento_ia: Optional[GroupingOutput] = None
    acoes_customizadas: Optional[dict] = None 
    status: str
