from ..models.times_model import times_bd, times_model,user_team_model
from ..repository.times_repository import times_repository
from ..repository.userteam_repository import userteam_repository
from ..repository.usuario_repository import user_repository
from ..repository.profile_repository import profille_repository

class times_services(object):
    _times_repository: times_repository = times_repository()
    _usuario_repository: user_repository = user_repository()
    _userteam_repository: userteam_repository = userteam_repository()
    _profiles_repository: profille_repository = profille_repository()
    
    def __init__(self):
        pass

    def buscar_times(self):
        return self._times_repository.get()

    def buscar_id_times(self, id):
        return self._times_repository.busca_id_times(id)

    def post_times(self, model: times_model):
        modelToInsert = times_bd()
        modelToInsert.id = model.id;
        modelToInsert.times = model.times;
        self._times_repository.post_times(modelToInsert)

        self.create_user_team(modelToInsert.id, model.times_model);

    def put_times(self, objectToPut: times_model):
        return self._times_repository.put_times(objectToPut)

    def delete_id_times(self, id: int):
        return self ._times_repository.delete_id_times(id)

    def create_user_team(self,idGroup:int, userTeams:list[user_team_model]):
        for userTeam in userTeams:
            userTeam.id_group = idGroup
            self._userteam_repository.create(userTeam)