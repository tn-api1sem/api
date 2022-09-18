from ..models.usuario_model import usuario_model
from ..repository.usuario_repository import user_repository


class usuario_services(object):
    _user_repository:user_repository = user_repository()
    def __init__(self):
        pass;

    def buscar_usuario(self):
        return self._user_repository.get()

    def buscar_id_usuario(self,id):
        return self._user_repository.busca_id_usuario(id)

    def post_usuario(self, objectToPost: usuario_model):
        return self._user_repository.post_usuario(objectToPost)

    def put_usuario(self, objectToPut: usuario_model):
        return self._user_repository.put_usuario(objectToPut)

    def delete_id_usuario(self, id:int):
       return self ._user_repository.delete_id_usuario(id)


