
from ..repository.usuario_repository import user_repository
from ..models.usuario_model import usuario_model


class usuario_services(object):
    _user_repository: user_repository = user_repository()

    def __init__(self):
        pass;

    def buscar_usuario(self):
        return self._user_repository.get()

    def buscar_id_usuario(self, id):
        return self._user_repository.busca_id_usuario(id)

    def post_usuario(self, objectToPost: usuario_model):
        if self._valida_geral(objectToPost):
            raise Exception("Insira todos os campos corretamente")
        return self._user_repository.post_usuario(objectToPost)

    def put_usuario(self, objectToPut: usuario_model):
        if self._valida_geral(objectToPut):
            raise Exception("Insira todos os campos corretamente")
        return self._user_repository.put_usuario(objectToPut)

    def delete_id_usuario(self, id: int):
        return self._user_repository.delete_id_usuario(id)

    def _valida_geral(self, model: usuario_model):
        if not model.email or not model.celular or not model.usuario or not model.senha:
            return True
        return False


