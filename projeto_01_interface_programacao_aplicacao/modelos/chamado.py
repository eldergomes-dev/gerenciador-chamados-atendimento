from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from configuracoes.banco_dados import BaseDeclarativa


class ModeloChamado(BaseDeclarativa):
    __tablename__ = "chamados"

    identificador = Column(Integer, primary_key=True, index=True)
    titulo = Column(String(200), nullable=False)
    descricao = Column(Text, nullable=False)
    categoria = Column(String(100), nullable=False)  # Ex: "Sistemas", "Hardware", "Redes"
    prioridade = Column(String(50), nullable=False, default="media")  # "baixa", "media", "alta", "critica"
    status_chamado = Column(String(50), nullable=False, default="aberto")  # "aberto", "em_atendimento", "resolvido", "fechado"
    
    identificador_solicitante = Column(Integer, ForeignKey("usuarios.identificador"), nullable=False)
    identificador_tecnico = Column(Integer, ForeignKey("usuarios.identificador"), nullable=True)

    data_abertura = Column(DateTime(timezone=True), server_default=func.now())
    data_atualizacao = Column(DateTime(timezone=True), onupdate=func.now())
    data_conclusao = Column(DateTime(timezone=True), nullable=True)

    usuario_solicitante = relationship(
        "ModeloUsuario",
        back_populates="chamados_criados",
        foreign_keys=[identificador_solicitante],
    )
    tecnico_responsavel = relationship(
        "ModeloUsuario",
        back_populates="chamados_atribuidos",
        foreign_keys=[identificador_tecnico],
    )