from  src.repository.context.api_context import ApiContext

class profile_repository(object):
    _apiContext: ApiContext = ApiContext()

    def __init__(self) -> None:
        pass

    def get(self):
        return self._apiContext.user_table.get_all()

    def busca_id_profile(self,id):
        return self._apiContext.profile_table.get(id)


    def post_profile(self, objectPost):
        self._apiContext.profile_table.begin_transaction()
        self._apiContext.profile_table.insert(objectPost)
        self._apiContext.profile_table.commit()

    def put_profile(self, objectPut):
        self._apiContext.profile_table.begin_transaction()
        self._apiContext.profile_table.commit()
        self._apiContext.user_table.begin_transaction()
        self._apiContext.user_table.update(objectPut)
        self._apiContext.user_table.commit()


    def delete_id_usuario(self, id:int):
        self._apiContext.user_table.begin_transaction()
        self._apiContext.user_table.delete(id)
        self._apiContext.user_table.commit()

