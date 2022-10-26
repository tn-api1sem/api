from ..models.avaliacaoUsuario_model import avaliacaoUsuario_model
from ..repository.avaliacaoUsuario_repository import avaliacaoUsuario_repository


class avaliacaoUsuario_service(object):
    _avaliacaoUsuario_repository: avaliacaoUsuario_repository = avaliacaoUsuario_repository()

    def __init__(self):
        pass

    def buscar_avaliacaoUsuario(self):
        return self._avaliacaoUsuario_repository.get()

    def buscar_id_avaliacaoUsuario(self, id):
        return self._avaliacaoUsuario_repository.buscar_id_avaliacaoUsuario(id)

    def post_avaliacaoUsuario(self, objectToPost: avaliacaoUsuario_model):
        return self._avaliacaoUsuario_repository.post_avaliacaoUsuario(objectToPost)

    def put_avaliacaoUsuario(self, objectToPut: avaliacaoUsuario_model):
        return self._avaliacaoUsuario_repository.put_avaliacaoUsuario(objectToPut)

    def delete_id_avaliacaoUsuario(self, id: int):
        return self._avaliacaoUsuario_repository.delete_id_avaliacaoUsuario(id)
