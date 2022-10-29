from ..models.times_model import times_model,user_team_model
from ..repository.times_repository import times_repository
from ..repository.userteam_repository import userteam_repository
from ..repository.usuario_repository import user_repository
from ..repository.profile_repository import profille_repository


class times_services(object):
    _times_repository: times_repository = times_repository()
    _userteam_repository: userteam_repository = userteam_repository
    _users_repository: user_repository  = user_repository()
    _profiles_repository: profille_repository = profille_repository()

    def __init__(self):
        pass


class times_services(object):
    _times_repository: times_repository = times_repository()
    _usuario_repository: user_repository = user_repository()
    _userteam_repository: userteam_repository = userteam_repository()

    def __init__(self):
        pass

    def buscar_times(self):
        return self._times_repository.get()

    def buscar_id_times(self, id):
        return self._times_repository.busca_id_times(id)

    def post_times(self, objectToPost: times_model):
        return self._times_repository.post_times(objectToPost)

    def put_times(self, objectToPut: times_model):
        return self._times_repository.put_times(objectToPut)

    def delete_id_times(self, id: int):
        return self ._times_repository.delete_id_times(id)

#inserindo a id do time e do e do id_users(userteam_mode)
    def create_id(self, id: user_team_model):
       listid = user_team_model.id
       for id in listid:
           Id = self._userteam_repository.busca_id_times(id)
           self._userteam_repository.busca_id_times(id)

    def create_id_users(self,id_users:user_team_model):
        listidusers = user_team_model.id_users
        for id_users in listidusers:
            idUsers = self._userteam_repository.busca_id_users(id_users)
            self._userteam_repository.busca_id_users(id_users)

    def create_team_id(self,team_id:user_team_model):
        listteamid = user_team_model.team_id
        for team_id in listteamid:
            teamId = self._userteam_repository.busca_team_id(team_id)
            self._userteam_repository.busca_team_id(team_id)

    def create_id_profile(self,id_profile:user_team_model):
        profileid = user_team_model.id_profile
        for id_profile in profileid:
            profileId = self._userteam_repository.post_id_profile(id_profile)
            self._userteam_repository.post_id_profile(id_profile)