from ..models.profile_model import profile_model
from ..repository.profile_repository import profille_repository


class profile_services(object):
    _profille_repository:profille_repository = profille_repository()
    def __init__(self):
        pass;

    def buscar_usuario(self):
        return self._profille_repository.get()

    def buscar_id_usuario(self,id):
        return self._profille_repository.busca_id_usuario(id)

    def post_usuario(self, objectToPost: profile_model):
        return self._profile_repository.post_usuario(objectToPost)

    def put_usuario(self, objectToPut: profile_model):
        return self._profile_repository.put_usuario(objectToPut)

    def delete_id_usuario(self, id:int):
       return self ._profile_repository.delete_id_usuario(id)
