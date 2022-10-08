from .context.api_context import ApiContext

class SprintsRepository(object):
    _apiContext: ApiContext

    def __init__(self) -> None:
        self._apiContext = ApiContext()
        pass

    def get(self):
        return self._apiContext.sprints_table.get_all()
    
    def get_by_id(self, id:int): 
        return self._apiContext.sprints_table.get(id)

    def create(self, objectToPost):
        self._apiContext.sprints_table.begin_transaction()
        self._apiContext.sprints_table.insert(objectToPost)
        self._apiContext.sprints_table.commit()

    def update(self, objectToPut):
        self._apiContext.sprints_table.begin_transaction()
        self._apiContext.sprints_table.update(objectToPut)
        self._apiContext.sprints_table.commit()

    def delete(self, id:int):
        self._apiContext.sprints_table.begin_transaction()
        self._apiContext.sprints_table.delete(id)
        self._apiContext.sprints_table.commit()


