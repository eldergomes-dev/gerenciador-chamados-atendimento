import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

load_dotenv()

endereco_banco = os.getenv(
    "ENDERECO_BANCO_DADOS", "sqlite:///./banco_dados_chamados.db"
)

mecanismo_banco = create_engine(
    endereco_banco,
    connect_args={"check_same_thread": False}
    if "sqlite" in endereco_banco
    else {},
)

SessaoBancoDados = sessionmaker(
    autocommit=False, autoflush=False, bind=mecanismo_banco
)

BaseDeclarativa = declarative_base()


def obter_sessao_banco_dados():
    sessao = SessaoBancoDados()
    try:
        yield sessao
    finally:
        sessao.close()