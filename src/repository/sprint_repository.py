from .context.api_context import ApiContext
from datetime import date

class SprintsRepository(object):
    _apiContext: ApiContext


    def __init__(self) -> None:
        self._apiContext = ApiContext()
        pass

    def get(self):
        return self._apiContext.sprints_table.get_all()
    
    def get_by_id(self, id:int): 
        return self._apiContext.sprints_table.get(id)

    def get_sprint_finished(self, user_teams): 
        sprints = self._apiContext.sprints_table.get_all()

        finished_sprints = []

        for sprint in sprints:
            for team in user_teams:
                if sprint.team_id == team and sprint.end_date < str(date.today()):
                    finished_sprints.append(sprint)

        return finished_sprints

    def create(self, objectToPost):
        self._apiContext.sprints_table.begin_transaction()
        self._apiContext.sprints_table.insert(objectToPost)
        self._apiContext.sprints_table.commit()

    def update(self, objectToPut):
        self._apiContext.sprints_table.begin_transaction()
        self._apiContext.sprints_table.update(objectToPut)
        self._apiContext.sprints_table.commit()

    def delete(self, id:int):
        self._apiContext.sprints_table.begin_transaction()
        self._apiContext.sprints_table.delete(id)
        self._apiContext.sprints_table.commit()

    def get_sprint_by_id_team(self, team_id):
        sprints = self.get()

        returnObject = []
        for sprint in sprints:

            if sprint.team_id != team_id:
                continue

            returnObject.append(sprint)

        return returnObject