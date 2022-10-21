
from ..repository.usuario_repository import user_repository
from ..models.usuario_model import usuario_model
import re

class usuario_services(object):
    _user_repository: user_repository = user_repository()

    def __init__(self):
        pass;

    def buscar_usuario(self):
        return self._user_repository.get()

    def buscar_id_usuario(self, id):
        return self._user_repository.busca_id_usuario(id)

    def create(self, model: usuario_model):
        self._validate(model)
        return self._user_repository.post_usuario(model)

    def update(self, model: usuario_model):
        self._validate(model)
        return self._user_repository.put_usuario(model)

    def delete_by_id(self, id: int):
        return self._user_repository.delete_id_usuario(id)

    def _validate(self, model: usuario_model):
        if not model.email or not model.celular or not model.usuario or not model.senha:
            raise Exception("Insira todos os campos")

        if model.id_perfil < 0:
            raise Exception("Insira um perfil valido")

        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if not re.fullmatch(regex, model.email):
            raise Exception("Insira um com formato valido")

        return


