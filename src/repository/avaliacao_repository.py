from src.repository.context.api_context import ApiContext

class avaliacao_repository(object):
    _apiContext: ApiContext = ApiContext()

    def __init__(self) -> None:
        pass

    def get(self):
        return self._apiContext.avaliacao_table.get_all()

    def busca_id_avaliacao(self, id):
        return self._apiContext.avaliacao_table.get(id)

    def post_avaliacao(self, objectPost):
        self._apiContext.avaliacao_table.begin_transaction()
        self._apiContext.avaliacao_table.insert(objectPost)
        self._apiContext.avaliacao_table.commit()

    def put_avaliacao(self, objectPut):
        self._apiContext.avaliacao_table.begin_transaction()
        self._apiContext.avaliacao_table.update(objectPut)
        self._apiContext.avaliacao_table.commit()

    def delete_id_avaliacao(self, id: int):
        self._apiContext.avaliacao_table.begin_transaction()
        self._apiContext.avaliacao_table.delete(id)
        self._apiContext.avaliacao_table.commit()