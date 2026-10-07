from typing import List
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from configuracoes.banco_dados import obter_sessao_banco_dados
from esquemas.chamado import (
    EsquemaAberturaChamado,
    EsquemaAtualizacaoChamado,
    EsquemaRespostaChamado,
)
from servicos.chamado import (
    atualizar_dados_chamado,
    buscar_chamado_por_identificador,
    criar_novo_chamado,
    listar_todos_chamados,
)

roteador_chamados = APIRouter(prefix="/chamados", tags=["Chamados"])


@roteador_chamados.post(
    "/",
    response_model=EsquemaRespostaChamado,
    status_code=status.HTTP_201_CREATED,
)
def abrir_chamado(
    dados_chamado: EsquemaAberturaChamado,
    identificador_solicitante: int,
    sessao_banco: Session = Depends(obter_sessao_banco_dados),
):
    return criar_novo_chamado(
        dados_chamado, identificador_solicitante, sessao_banco
    )


@roteador_chamados.get("/", response_model=List[EsquemaRespostaChamado])
def listar_chamados(
    sessao_banco: Session = Depends(obter_sessao_banco_dados),
):
    return listar_todos_chamados(sessao_banco)


@roteador_chamados.get(
    "/{identificador_chamado}", response_model=EsquemaRespostaChamado
)
def obter_chamado(
    identificador_chamado: int,
    sessao_banco: Session = Depends(obter_sessao_banco_dados),
):
    return buscar_chamado_por_identificador(identificador_chamado, sessao_banco)


@roteador_chamados.put(
    "/{identificador_chamado}", response_model=EsquemaRespostaChamado
)
def atualizar_chamado(
    identificador_chamado: int,
    dados_atualizacao: EsquemaAtualizacaoChamado,
    sessao_banco: Session = Depends(obter_sessao_banco_dados),
):
    return atualizar_dados_chamado(
        identificador_chamado, dados_atualizacao, sessao_banco
    )