from ..models.times_model import times_model
from ..repository.times_repository import times_repository


class times_services(object):
    _times_repository: times_repository = times_repository()

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
