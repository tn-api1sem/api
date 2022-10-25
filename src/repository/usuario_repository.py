from  src.repository.context.api_context import ApiContext

class user_repository(object):
    _apiContext: ApiContext = ApiContext()

    def __init__(self) -> None:
        pass

    def get(self):
        return self._apiContext.user_table.get_all()

    def get_by_id(self,id):
        return self._apiContext.user_table.get(id)

    def post_usuario(self, objectPost):
        self._apiContext.user_table.begin_transaction()
        self._apiContext.user_table.insert(objectPost)
        self._apiContext.user_table.commit()

    def put_usuario(self, objectPut):
        self._apiContext.user_table.begin_transaction()
        self._apiContext.user_table.update(objectPut)
        self._apiContext.user_table.commit()

    def delete_id_usuario(self, id:int):
        self._apiContext.user_table.begin_transaction()
        self._apiContext.user_table.delete(id)
        self._apiContext.user_table.commit()

