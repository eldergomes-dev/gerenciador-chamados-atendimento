from typing import List
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from configuracoes.banco_dados import obter_sessao_banco_dados
from esquemas.usuario import EsquemaCriacaoUsuario, EsquemaRespostaUsuario
from servicos.usuario import criar_novo_usuario, listar_todos_usuarios

roteador_usuarios = APIRouter(prefix="/usuarios", tags=["Usuários"])


@roteador_usuarios.post(
    "/",
    response_model=EsquemaRespostaUsuario,
    status_code=status.HTTP_201_CREATED,
)
def cadastrar_usuario(
    dados_usuario: EsquemaCriacaoUsuario,
    sessao_banco: Session = Depends(obter_sessao_banco_dados),
):
    return criar_novo_usuario(dados_usuario, sessao_banco)


@roteador_usuarios.get("/", response_model=List[EsquemaRespostaUsuario])
def listar_usuarios(
    sessao_banco: Session = Depends(obter_sessao_banco_dados),
):
    return listar_todos_usuarios(sessao_banco)