from src.repository.context.api_context import ApiContext


class times_repository(object):
    _apiContext: ApiContext = ApiContext()

    def __init__(self) -> None:
        pass

    def get(self):
        return self._apiContext.times_table.get_all()

    def busca_id_times(self, id):
        return self._apiContext.times_table.get(id)

    def post_times(self, objectPost):
        self._apiContext.times_table.begin_transaction()
        self._apiContext.times_table.insertTeams(objectPost)
        self._apiContext.times_table.commit()

    def put_times(self, objectPut):
        self._apiContext.times_table.begin_transaction()
        self._apiContext.times_table.update(objectPut)
        self._apiContext.times_table.commit()

    def delete_id_times(self, id: int):
        self._apiContext.times_table.begin_transaction()
        self._apiContext.times_table.delete(id)
        self._apiContext.times_table.commit()
