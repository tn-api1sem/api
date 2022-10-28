from ..models.times_model import times_model
from ..repository.times_repository import times_repository
from ..repository.usuario_repository import user_repository


class times_services(object):
    _times_repository: times_repository = times_repository()
    _usuario_repository: user_repository = user_repository()

    def __init__(self):
        pass

    def buscar_times(self):
        return self._times_repository.get()

    def buscar_id_times(self, id):
        return self._times_repository.busca_id_times(id)

    def post_times(self, objectToPost: times_model):
        return self._times_repository.post_times(objectToPost)

    def put_times(self, objectToPut: times_model):
        return self._times_repository.put_times(objectToPut)

    def delete_id_times(self, id: int):
        return self ._times_repository.delete_id_times(id)

    def create(self, id: times_model):
        # obtem os id's que foram salvos na team.json
        listUser = times_model.id_users
        # percorre a lista
        for user in listUser:
            # busca os dados da tabela users
            usuario = self._usuario_repository.busca_id_usuario(user)
            # insere
            self._usuario_repository.post_usuario(usuario)
