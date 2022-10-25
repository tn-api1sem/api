from ..models.avaliacao_model import avaliacao_model
from ..repository.avaliacao_repository import avaliacao_repository

class avaliacao_services(object):
    _avaliacao_repository: avaliacao_repository = avaliacao_repository()

    def __init__(self):
        pass

    def buscar_avaliacao(self):
        return self._avaliacao_repository.get()

    def buscar_id_avaliacao(self, id):
        return self._avaliacao_repository.busca_id_avaliacao(id)

    def post_avaliacao(self, objectToPost: times_model):
        return self._avaliacao_repository.post_avaliacao(objectToPost)

    def put_avaliacao(self, objectToPut: times_model):
        return self._avaliacao_repository.put_avaliacao(objectToPut)

    def delete_id_avaliacao(self, id: int):
        return self ._avaliacao_repository.delete_id_avaliacao(id)