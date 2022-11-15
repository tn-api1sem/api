from ..models.times_model import times_bd, times_model, user_team_model
from ..repository.times_repository import times_repository
from ..repository.userteam_repository import userteam_repository
from ..repository.usuario_repository import user_repository
from ..repository.profile_repository import profille_repository


class dashboard_services(object):
    _times_repository: times_repository = times_repository()
    _usuario_repository: user_repository = user_repository()
    _userteam_repository: userteam_repository = userteam_repository()
    _profiles_repository: profille_repository = profille_repository()

    def __init__(self):
        pass

    def get_user_teams_by_user_id(self, id):
        return self._userteam_repository.get_user_teams_by_user_id(id)
