from src.repository.context.api_context import ApiContext


class userteam_repository(object):
    _apiContext: ApiContext = ApiContext()

    def __init__(self) -> None:
        pass

    def get_all(self):
        return self._apiContext.userTeam_table.get_all()

    def get_user_teams_by_team_id(self, team_id):
        userTeams = self.get_all()

        returnObject = []
        for userTeam in userTeams:

            if userTeam.id_team != team_id:
                continue

            returnObject.append(userTeam)

        return returnObject

    def get_user_teams_by_user_id(self, user_id):
        userTeams = self.get_all()

        returnObject = []
        for userTeam in userTeams:

            if userTeam.id_user != user_id:
                continue

            returnObject.append(userTeam)

        return returnObject

    def create(self, objectPost):
        self._apiContext.userTeam_table.begin_transaction()
        self._apiContext.userTeam_table.insert(objectPost)
        self._apiContext.userTeam_table.commit()

    def update(self, objectPut):
        self._apiContext.userTeam_table.begin_transaction()
        self._apiContext.userTeam_table.update(objectPut)
        self._apiContext.userTeam_table.commit()

    def delete(self, id: int):
        self._apiContext.userTeam_table.begin_transaction()
        self._apiContext.userTeam_table.delete(id)
        self._apiContext.userTeam_table.commit()
