from sqlalchemy import Boolean, Column, DateTime, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from configuracoes.banco_dados import BaseDeclarativa


class ModeloUsuario(BaseDeclarativa):
    __tablename__ = "usuarios"

    identificador = Column(Integer, primary_key=True, index=True)
    nome_completo = Column(String(150), nullable=False)
    endereco_email = Column(String(150), unique=True, index=True, nullable=False)
    senha_criptografada = Column(String(255), nullable=False)
    perfil_acesso = Column(String(50), nullable=False, default="cliente")  # "cliente", "tecnico", "administrador"
    usuario_ativo = Column(Boolean, default=True)
    data_criacao = Column(DateTime(timezone=True), server_default=func.now())

    chamados_criados = relationship(
        "ModeloChamado",
        back_populates="usuario_solicitante",
        foreign_keys="ModeloChamado.identificador_solicitante",
    )
    chamados_atribuidos = relationship(
        "ModeloChamado",
        back_populates="tecnico_responsavel",
        foreign_keys="ModeloChamado.identificador_tecnico",
    )