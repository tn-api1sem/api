from ..models.grupo_model import grupo_model
from ..repository.grupo_repository import grupo_repository
from ..repository.usuario_repository import user_repository


class grupo_services(object):
    _grupo_repository: grupo_repository =grupo_repository()
    _users_repository: user_repository  = user_repository()

    def __init__(self):
        pass

    def buscar_grupo(self):
        grupo = self._grupo_repository.get();

        for grupo in grupo:
            grupo.usuarios = []
            for userId in grupo.id_users:
                user = self._users_repository.get_by_id(userId)
                grupo.usuarios.append(user.usuario)

        return grupo

    def buscar_id_grupo(self, id):
        return self._grupo_repository.busca_id_times(id)

    def post_grupo(self, objectToPost: grupo_model):
        return self._grupo_repository.post_grupo(objectToPost)

    def put_grupo(self, objectToPut: grupo_model):
        return self._grupo_repository.put_grupo(objectToPut)

    def delete_id_grupo(self, id: int):
        return self ._grupo_repository.delete_id_grupo(id)
