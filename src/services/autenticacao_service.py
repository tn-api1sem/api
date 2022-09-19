from distutils.log import error
from src.models.login_model import autenticacao_model
from src.repository.autenticacao_repository import user_repository

class autenticacao_service(object):
    repository:user_repository = user_repository()

    def __init__(self) -> None:
        pass

    def login (self, login:autenticacao_model):
        todos_usuarios = self.repository.get()
        for usuario in todos_usuarios:
            if usuario.usuario == login.usuario and usuario.senha == login.senha:
                return usuario

        raise Exception("Usuario/Senhas incorretos")