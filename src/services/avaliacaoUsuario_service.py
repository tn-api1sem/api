from datetime import datetime
from ..models.avaliacaoUsuario_model import avaliacaoUsuario_model
from ..repository.avaliacaoUsuario_repository import avaliacaoUsuario_repository
from ..repository.sprint_repository import SprintsRepository


class avaliacaoUsuario_service(object):
    _avaliacaoUsuario_repository: avaliacaoUsuario_repository = avaliacaoUsuario_repository()
    _sprint_repository: SprintsRepository = SprintsRepository()

    def __init__(self):
        pass

    def buscar_avaliacaoUsuario(self):
        return self._avaliacaoUsuario_repository.get()

    def buscar_id_avaliacaoUsuario(self, id):
        return self._avaliacaoUsuario_repository.buscar_id_avaliacaoUsuario(id)

    def post_avaliacaoUsuario(self, model: avaliacaoUsuario_model):
        self.validaCadastro(model)
        self._avaliacaoUsuario_repository.post_avaliacaoUsuario(model)
        return

    def put_avaliacaoUsuario(self, model: avaliacaoUsuario_model):
        self.validaCadastro(model)
        self._avaliacaoUsuario_repository.put_avaliacaoUsuario(model)
        return

    def delete_id_avaliacaoUsuario(self, id: int):
        return self._avaliacaoUsuario_repository.delete_id_avaliacaoUsuario(id)

    def validaCadastro(self, model: avaliacaoUsuario_model):
        sprint = self._sprint_repository.get_by_id(model.sprint_id)

        end_date = datetime.strptime(sprint.evaluation_range, '%Y-%m-%d')

        if end_date < datetime.now():
            raise Exception("Data de fim da sprint deve ser menor que data de começo da sprint")
            
