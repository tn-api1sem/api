from ..models.times_model import times_model
from ..repository.times_repository import times_repository
from ..repository.usuario_repository import user_repository
from ..repository.profile_repository import profille_repository


class times_services(object):
    _times_repository: times_repository = times_repository()
    _users_repository: user_repository  = user_repository()
    _profiles_repository: profille_repository = profille_repository()

    def __init__(self):
        pass

    def buscar_times(self):
        times = self._times_repository.get();

        for time in times:
            time.usuarios = []
            for userId in time.id_users:
                user = self._users_repository.get_by_id(userId)
                time.usuarios.append(user.usuario)

        return times

    def buscar_id_times(self, id):
        id_times = self._times_repository.busca_id_times()

        for time in id_times:
            time.id_times = []
            for teamId in time.team_id:
                team = self._times_repository.get_by_id(teamId)
                time.times.append(team.usuario)
              #  with open("teams.json", encoding="utf-8") as arq:
               #     time.times.append(team.usuario)

        return id_times

    def buscar_id_profile(self, id):
        id_profile = self._times_repository.busca_id_profile()

        for profile in id_profile:
            profile.id_profile = []
            for profileId in profile.id_profile:
                profile = self._repository.get_by_id(profileId)
                profile.id_profile.append(profile.usuario)

        return id_profile

    def post_times(self, objectToPost: times_model):
        return self._times_repository.post_times(objectToPost)

    def put_times(self, objectToPut: times_model):
        return self._times_repository.put_times(objectToPut)

    def delete_id_times(self, id: int):
        return self ._times_repository.delete_id_times(id)
