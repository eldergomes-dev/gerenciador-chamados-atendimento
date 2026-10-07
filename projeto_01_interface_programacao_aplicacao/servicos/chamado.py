from datetime import datetime
from typing import List
from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from esquemas.chamado import EsquemaAberturaChamado, EsquemaAtualizacaoChamado
from modelos.chamado import ModeloChamado


def criar_novo_chamado(
    dados_chamado: EsquemaAberturaChamado,
    identificador_solicitante: int,
    sessao_banco: Session,
) -> ModeloChamado:
    novo_chamado = ModeloChamado(
        titulo=dados_chamado.titulo,
        descricao=dados_chamado.descricao,
        categoria=dados_chamado.categoria,
        prioridade=dados_chamado.prioridade,
        identificador_solicitante=identificador_solicitante,
    )

    sessao_banco.add(novo_chamado)
    sessao_banco.commit()
    sessao_banco.refresh(novo_chamado)

    return novo_chamado


def listar_todos_chamados(sessao_banco: Session) -> List[ModeloChamado]:
    return sessao_banco.query(ModeloChamado).all()


def buscar_chamado_por_identificador(
    identificador_chamado: int, sessao_banco: Session
) -> ModeloChamado:
    chamado = (
        sessao_banco.query(ModeloChamado)
        .filter(ModeloChamado.identificador == identificador_chamado)
        .first()
    )

    if not chamado:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Chamado não encontrado no sistema.",
        )

    return chamado


def atualizar_dados_chamado(
    identificador_chamado: int,
    dados_atualizacao: EsquemaAtualizacaoChamado,
    sessao_banco: Session,
) -> ModeloChamado:
    chamado = buscar_chamado_por_identificador(identificador_chamado, sessao_banco)

    dados_dict = dados_atualizacao.model_dump(exclude_unset=True)

    for campo, valor in dados_dict.items():
        setattr(chamado, campo, valor)

    if dados_atualizacao.status_chamado in ["resolvido", "fechado"]:
        chamado.data_conclusao = datetime.now()

    sessao_banco.commit()
    sessao_banco.refresh(chamado)

    return chamado