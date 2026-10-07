from datetime import datetime
from typing import Optional
from pydantic import BaseModel, EmailStr


class EsquemaCriacaoUsuario(BaseModel):
    nome_completo: str
    endereco_email: EmailStr
    senha_plana: str
    perfil_acesso: Optional[str] = "cliente"


class EsquemaRespostaUsuario(BaseModel):
    identificador: int
    nome_completo: str
    endereco_email: EmailStr
    perfil_acesso: str
    usuario_ativo: bool
    data_criacao: datetime

    class Config:
        from_attributes = True