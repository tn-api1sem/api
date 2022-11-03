from src.repository.context.api_context import ApiContext


class userteam_repository(object):
    _apiContext: ApiContext = ApiContext()

    def __init__(self) -> None:
        pass



#######Fazendo a insercao dos outros campo do userteam_model (id_users e username)
    def busca_id_times(self,id):
        return self._apiContext.userTeam_table.get(id)

    def busca_id_users(self, id_users):
        return self._apiContext.userTeam_table.get(id_users)

#team_id e id_profile#
    def busca_team_id(self, team_id):
        return self._apiContext.userTeam_table.get(team_id)


    def create(self, objectPost):
        self._apiContext.userTeam_table.begin_transaction()
        self._apiContext.userTeam_table.insert(objectPost)
        self._apiContext.userTeam_table.commit()

    def put_id_profile(self, objectPut):
        self._apiContext.userTeam_table.begin_transaction()
        self._apiContext.userTeam_table.update(objectPut)
        self._apiContext.userTeam_table.commit()

    def delete_id_profile(self, id: int):
        self._apiContext.userTeam_table.begin_transaction()
        self._apiContext.userTeam_table.delete(id)
        self._apiContext.userTeam_table.commit()



