from ..models.times_model import times_model
from ..repository.userteam_repository import userteam_repository


class userteam_services(object):
    _userteam_repository: userteam_repository = times_repository()

    def __init__(self):
        pass

    def buscar_times(self):
        return self._userteam_repository.get()

    def buscar_id_times(self, id):
        return self._userteam_repository.busca_id_times(id)

    def post_times(self, objectToPost: times_model):
        return self._userteam_repository.post_times(objectToPost)

    def put_times(self, objectToPut: times_model):
        return self._userteam_repository.put_times(objectToPut)

    def delete_id_times(self, id: int):
        return self ._userteam_repository.delete_id_times(id)
