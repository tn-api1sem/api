from datetime import datetime
from src.models.sprints_model import SprintsModel
from src.repository.sprint_repository import SprintsRepository


class SprintService(object):
    repository:SprintsRepository = SprintsRepository()
    
    def __init__(self) -> None:
        pass

    def get(self):
        return self.repository.get()
        
    def get_by_id(self, id:int) -> SprintsModel: 
        return self.repository.get_by_id(id)

    def create(self, model: SprintsModel):
        self._validate(model);
        self.repository.create(model)
        return

    def update(self, model: SprintsModel):
        self._validate(model);
        self.repository.update(model)
        return;

    def delete(self, id:int) -> None:
        self.repository.delete(id)
        return;

    def _validate(self, model: SprintsModel):
        if not model.end_date or not model.start_date or not model.evaluation_range or not model.name or model.team_id == -1:
            raise Exception("Insira todos os campos corretamente")

        start_date_time = datetime.strptime(model.start_date, '%Y-%m-%d')
        end_date_time = datetime.strptime(model.end_date, '%Y-%m-%d')
        evaluation_range_date_time = datetime.strptime(model.evaluation_range, '%Y-%m-%d')

        if start_date_time >= end_date_time:
            raise Exception("Data de fim da sprint deve ser menor que data de começo da sprint")

        if evaluation_range_date_time <= end_date_time or evaluation_range_date_time <= start_date_time:
            raise Exception("Data de fim da avaliação deve ser posterior que o final da sprint")

        return;