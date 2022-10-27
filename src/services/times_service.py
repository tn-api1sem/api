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

# popular a tabela em um crud#
# Aqui to fazendo a busca
    def buscar_id_times(self, id):
        id_times = self._times_repository.busca_id_times()

        for time in id_times:
            time.id_times = []
            for teamId in time.team_id:
                team = self._times_repository.get_by_id(teamId)
                time.times.append(team.usuario)

        return id_times

    def post_id_times(self,id):
        id_times = self._times_repository.pos_id_times()

        for time in id_times:
            time.id_times = []
            for teamId in time.team_id:
                team = self._times_repository.get_by_id(teamId)
                time.times.append(team.usuario)

        return id_times


