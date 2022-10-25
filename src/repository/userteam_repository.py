from src.repository.context.api_context import ApiContext


class userteam_repository(object):
    _apiContext: ApiContext = ApiContext()

    def __init__(self) -> None:
        pass

    def get(self):
        return self._apiContext.times_table.get_all()

    def busca_id_userteam(self, id):
        return self._apiContext.userteam_table.get(id)

    def post_times(self, objectPost):
        self._apiContext.userteam.begin_transaction()
        self._apiContext.userteam.insert(objectPost)
        self._apiContext.userteam.commit()

    def put_times(self, objectPut):
        self._apiContext.userteam.begin_transaction()
        self._apiContext.userteam.update(objectPut)
        self._apiContext.userteam.commit()

    def delete_id_times(self, id: int):
        self._apiContext.userteam.begin_transaction()
        self._apiContext.userteam.delete(id)
        self._apiContext.userteam.commit()
