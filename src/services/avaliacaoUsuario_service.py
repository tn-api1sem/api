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

    def get_already_rated_sprints(self, userId):
        rates = self._avaliacaoUsuario_repository.get();

        sprintsAlreadyRated = [];
        sprintsIds = []

        for a in rates:
           if  userId == a.rated_by and a.sprint_id not in sprintsIds:
                sprint = self._sprint_repository.get_by_id(int(a.sprint_id));
                sprintsAlreadyRated.append(sprint)
                sprintsIds.append(sprint.id)

        return sprintsAlreadyRated;
        
    def buscar_sprint_id_avaliacaoUsuario(self, sprint_id):
        return self._avaliacaoUsuario_repository.buscar_sprint_id_avaliacaoUsuario(sprint_id)

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

        end_datetime = datetime.strptime(sprint.evaluation_range, '%Y-%m-%d')
        end_date = datetime.date(end_datetime)
        today = datetime.date(datetime.today())

        if end_date < today:
            raise Exception(
                "A avaliação só poderá ser cadastrada durante o período de avaliação da sua respectiva sprint")
