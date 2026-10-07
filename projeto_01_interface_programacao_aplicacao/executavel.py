from fastapi import FastAPI
from configuracoes.banco_dados import BaseDeclarativa, mecanismo_banco
import modelos
from rotas import roteador_chamados, roteador_usuarios

# Cria as tabelas no banco caso não existam
BaseDeclarativa.metadata.create_all(bind=mecanismo_banco)

aplicacao = FastAPI(
    title="Sistema de Gerenciamento de Chamados e Atendimento",
    description="API corporativa para controle de chamados, suporte técnico e acompanhamento de solicitações.",
    version="1.0.0",
)

# Inclusão dos roteadores de Usuários e Chamados
aplicacao.include_router(roteador_usuarios)
aplicacao.include_router(roteador_chamados)


@aplicacao.get("/")
def verificar_status_aplicacao():
    return {
        "mensagem": "API do Gerenciador de Chamados rodando com sucesso!",
        "status": "Ativo",
    }