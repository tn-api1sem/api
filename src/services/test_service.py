from ..models import test_model 
from ..repository.test_repository import test_repository


class test_service(object):
    repository:test_repository = test_repository()
    
    def __init__(self) -> None:
        pass

    def get(self):
        return self.repository.get()
        
    def get_by_id(self, id:int) -> test_model: 
        return self.repository.get_by_id(id)

    def post(self, objectToPost: test_model):
        self.repository.post(objectToPost)
        return

    def put(self, objectToPut: test_model):
        self.repository.put(objectToPut)
        return;

    def delete(self, id:int) -> None:
        self.repository.delete(id)
        return;
