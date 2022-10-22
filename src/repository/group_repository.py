from .context.api_context import ApiContext

class GroupRepository(object):
    _apiContext: ApiContext

    def __init__(self) -> None:
        self._apiContext = ApiContext()
        pass

    def get(self):
        return self._apiContext.group_table.get_all()
    
    def get_by_id(self, id:int): 
        return self._apiContext.group_table.get(id)

    def create(self, model):
        self._apiContext.group_table.begin_transaction()
        self._apiContext.group_table.insert(model)
        self._apiContext.group_table.commit()

    def update(self, model):
        self._apiContext.group_table.begin_transaction()
        self._apiContext.group_table.update(model)
        self._apiContext.group_table.commit()

    def delete(self, id:int):
        self._apiContext.group_table.begin_transaction()
        self._apiContext.group_table.delete(id)
        self._apiContext.group_table.commit()


