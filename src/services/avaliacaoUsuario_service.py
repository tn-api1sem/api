from datetime import datetime
from ..models.avaliacaoUsuario_model import avaliacaoUsuario_model
from ..repository.avaliacaoUsuario_repository import avaliacaoUsuario_repository
from ..repository.avaliacao_repository import avaliacao_repository
from ..repository.sprint_repository import SprintsRepository


class avaliacaoUsuario_service(object):
    _avaliacaoUsuario_repository: avaliacaoUsuario_repository = avaliacaoUsuario_repository()
    _avaliacao_repository: avaliacao_repository = avaliacao_repository()
    _sprint_repository: SprintsRepository = SprintsRepository()

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

    def validaCadastro(self, model: avaliacaoUsuario_model):
        sprint = self._sprint_repository.get_by_id(
            avaliacaoUsuario_model.sprint_id)

        end_date = datetime.strptime(sprint.end_date, '%Y-%m-%d')

        if end_date < datetime.now:
            raise Exception(
                "Data de fim da sprint deve ser menor que data de começo da sprint")
            return
