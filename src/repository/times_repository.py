from src.repository.context.api_context import ApiContext


class times_repository(object):
    _apiContext: ApiContext = ApiContext()

    def __init__(self) -> None:
        pass

    def get(self):
        return self._apiContext.times_table.get_all()
#times e sua id
    def busca_id_times(self, id):
        return self._apiContext.times_table.get(id)

    def post_times(self, objectPost):
        self._apiContext.times_table.begin_transaction()
        self._apiContext.times_table.insert(objectPost)
        self._apiContext.times_table.commit()
#inserindo a id do time
    def post_id_times(self, objectPost):
        self._apiContext.times_table.begin_transaction()
        self._apiContext.times_table.insert(objectPost)
        self._apiContext.times_table.commit()


    def put_times(self, objectPut):
        self._apiContext.times_table.begin_transaction()
        self._apiContext.times_table.update(objectPut)
        self._apiContext.times_table.commit()


    def delete_id_times(self, id: int):
        self._apiContext.times_table.begin_transaction()
        self._apiContext.times_table.delete(id)
        self._apiContext.times_table.commit()


#######Fazendo a insercao dos outros campo do times_model (id_users e username)
    def busca_id_users(self, id_users):
        return self._apiContext.times_table.get(id_users)

    def get_username(self,username):
        return self._apiContext.times_table.get(username)


    def post_username(self, objectPost):
        self._apiContext.times_table.begin_transaction()
        self._apiContext.times_table.insert(objectPost)
        self._apiContext.times_table.commit()

    def put_username(self, objectPut):
        self._apiContext.times_table.begin_transaction()
        self._apiContext.times_table.update(objectPut)
        self._apiContext.times_table.commit()

    def delete_id_users(self, id: list[int]):
        self._apiContext.times_table.begin_transaction()
        self._apiContext.times_table.delete(id)
        self._apiContext.times_table.commit()

#team_id e id_profile#
    def busca_team_id(self, team_id):
        return self._apiContext.times_table.get(team_id)


    def post_id_profile(self, objectPost):
        self._apiContext.times_table.begin_transaction()
        self._apiContext.times_table.insert(objectPost)
        self._apiContext.times_table.commit()

    def put_id_profile(self, objectPut):
        self._apiContext.times_table.begin_transaction()
        self._apiContext.times_table.update(objectPut)
        self._apiContext.times_table.commit()

    def delete_id_profile(self, id: list[int]):
        self._apiContext.times_table.begin_transaction()
        self._apiContext.times_table.delete(id)
        self._apiContext.times_table.commit()



