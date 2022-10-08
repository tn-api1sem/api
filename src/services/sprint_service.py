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
        self.repository.create(model)
        return

    def update(self, model: SprintsModel):
        self.repository.update(model)
        return;

    def delete(self, id:int) -> None:
        self.repository.delete(id)
        return;
