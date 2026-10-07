from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from esquemas.usuario import EsquemaRespostaUsuario


class EsquemaAberturaChamado(BaseModel):
    titulo: str
    descricao: str
    categoria: str
    prioridade: Optional[str] = "media"


class EsquemaAtualizacaoChamado(BaseModel):
    titulo: Optional[str] = None
    descricao: Optional[str] = None
    categoria: Optional[str] = None
    prioridade: Optional[str] = None
    status_chamado: Optional[str] = None
    identificador_tecnico: Optional[int] = None


class EsquemaRespostaChamado(BaseModel):
    identificador: int
    titulo: str
    descricao: str
    categoria: str
    prioridade: str
    status_chamado: str
    identificador_solicitante: int
    identificador_tecnico: Optional[int] = None
    data_abertura: datetime
    data_atualizacao: Optional[datetime] = None
    data_conclusao: Optional[datetime] = None
    usuario_solicitante: Optional[EsquemaRespostaUsuario] = None
    tecnico_responsavel: Optional[EsquemaRespostaUsuario] = None

    class Config:
        from_attributes = True