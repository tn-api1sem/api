from .context.api_context import ApiContext

class test_repository(object):
    _apiContext: ApiContext

    def __init__(self) -> None:
        self._apiContext = ApiContext()
        pass

    def get(self):
        return self._apiContext.test_table.get_all()
    
    def get_by_id(self, id:int): 
        return self._apiContext.test_table.get(id)

    def post(self, objectToPost):
        self._apiContext.test_table.begin_transaction()
        self._apiContext.test_table.insert(objectToPost)
        self._apiContext.test_table.commit()

    def put(self, objectToPut):
        self._apiContext.test_table.begin_transaction()
        self._apiContext.test_table.update(objectToPut)
        self._apiContext.test_table.commit()

    def delete(self, id:int):
        self._apiContext.test_table.begin_transaction()
        self._apiContext.test_table.delete(id)
        self._apiContext.test_table.commit()


