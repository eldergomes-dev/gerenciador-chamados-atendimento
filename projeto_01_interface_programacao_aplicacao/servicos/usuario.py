import bcrypt
from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from esquemas.usuario import EsquemaCriacaoUsuario
from modelos.usuario import ModeloUsuario


def gerar_hash_senha(senha_plana: str) -> str:
    # Converte a senha para bytes e limita explicitamente em 72 bytes para o Bcrypt
    senha_bytes = senha_plana.encode("utf-8")[:72]
    sal_criptografico = bcrypt.gensalt()
    hash_bytes = bcrypt.hashpw(senha_bytes, sal_criptografico)
    return hash_bytes.decode("utf-8")


def criar_novo_usuario(
    dados_usuario: EsquemaCriacaoUsuario, sessao_banco: Session
) -> ModeloUsuario:
    usuario_existente = (
        sessao_banco.query(ModeloUsuario)
        .filter(ModeloUsuario.endereco_email == dados_usuario.endereco_email)
        .first()
    )

    if usuario_existente:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Já existe um usuário cadastrado com este e-mail.",
        )

    senha_criptografada = gerar_hash_senha(dados_usuario.senha_plana)

    novo_usuario = ModeloUsuario(
        nome_completo=dados_usuario.nome_completo,
        endereco_email=dados_usuario.endereco_email,
        senha_criptografada=senha_criptografada,
        perfil_acesso=dados_usuario.perfil_acesso,
    )

    sessao_banco.add(novo_usuario)
    sessao_banco.commit()
    sessao_banco.refresh(novo_usuario)

    return novo_usuario


def listar_todos_usuarios(sessao_banco: Session):
    return sessao_banco.query(ModeloUsuario).all()