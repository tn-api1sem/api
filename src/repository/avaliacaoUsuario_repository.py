from src.repository.context.api_context import ApiContext


class avaliacaoUsuario_repository(object):
    _apiContext: ApiContext = ApiContext()

    def __init__(self) -> None:
        pass

    def get(self):
        return self._apiContext.avaliacaoUsuario_table.get_all()

    def buscar_id_avaliacaoUsuario(self, id):
        return self._apiContext.avaliacaoUsuario_table.get(id)

    def post_avaliacaoUsuario(self, objectPost):
        self._apiContext.avaliacaoUsuario_table.begin_transaction()
        self._apiContext.avaliacaoUsuario_table.insert(objectPost)
        self._apiContext.avaliacaoUsuario_table.commit()

    def put_avaliacaoUsuario(self, objectPut):
        self._apiContext.avaliacaoUsuario_table.begin_transaction()
        self._apiContext.avaliacaoUsuario_table.update(objectPut)
        self._apiContext.avaliacaoUsuario_table.commit()

    def delete_id_avaliacaoUsuario(self, id: int):
        self._apiContext.avaliacaoUsuario_table.begin_transaction()
        self._apiContext.avaliacaoUsuario_table.delete(id)
        self._apiContext.avaliacaoUsuario_table.commit()
