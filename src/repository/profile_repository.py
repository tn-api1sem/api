from  src.repository.context.api_context import ApiContext

class profille_repository(object):
    _apiContext: ApiContext = ApiContext()

    def __init__(self) -> None:
        pass

    def get(self):
        return self._apiContext.profile_table.get_all()

    def find(self,id):
        return self._apiContext.profile_table.get(id)

    def create(self, objectPost):
        self._apiContext.profile_table.begin_transaction()
        self._apiContext.profile_table.insert(objectPost)
        self._apiContext.profile_table.commit()

    def update(self, objectPut):
        self._apiContext.profile_table.begin_transaction()
        self._apiContext.profile_table.commit()
        self._apiContext.profile_table.begin_transaction()
        self._apiContext.profile_table.update(objectPut)
        self._apiContext.profile_table.commit()


    def delete(self, id:int):
        self._apiContext.profile_table.begin_transaction()
        self._apiContext.profile_table.delete(id)
        self._apiContext.profile_table.commit()

