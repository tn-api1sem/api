from ..models.times_model import times_bd, times_model,user_team_model
from ..repository.times_repository import times_repository
from ..repository.userteam_repository import userteam_repository
from ..repository.usuario_repository import user_repository
from ..repository.profile_repository import profille_repository
<<<<<<< HEAD
=======

>>>>>>> origin/develop

class times_services(object):
    _times_repository: times_repository = times_repository()
    _usuario_repository: user_repository = user_repository()
<<<<<<< HEAD
    _userteam_repository: userteam_repository = userteam_repository()
    _profiles_repository: profille_repository = profille_repository()
    
=======

    _userteam_repository: userteam_repository = userteam_repository()
    _profiles_repository: profille_repository = profille_repository()
    

>>>>>>> origin/develop
    def __init__(self):
        pass

    def buscar_times(self):
        times = self._times_repository.get();
        return times;

    def buscar_id_times(self, id):
        time = self._times_repository.busca_id_times(id);
        user_teams = self._userteam_repository.get_user_teams_by_team_id(time.id);
        
        model = times_model();
        model.id = time.id;
        model.times = time.times;
        model.times_model = [];

        for u_t in user_teams:
            u_t.user = self._usuario_repository.get_by_id(u_t.id_user).usuario;
            u_t.profile = self._profiles_repository.find(u_t.id_profile).perfil

            model.times_model.append(u_t);

        return model;



    def post_times(self, model: times_model):
        modelToInsert = times_bd()
        modelToInsert.id = model.id;
        modelToInsert.times = model.times;
        self._times_repository.post_times(modelToInsert)

        self.create_user_team(modelToInsert.id, model.times_model);

    def put_times(self, model: times_model):
        modelToInsert = times_bd()
        modelToInsert.id = model.id;
        modelToInsert.times = model.times;

        self._times_repository.update(modelToInsert)
        self.update_user_team(modelToInsert.id, model.times_model);

    def delete_id_times(self, id: int):
        self.delete_id_times(id)
        return self ._times_repository.delete_id_times(id)
<<<<<<< HEAD

    def create(self, id: times_model):
        # obtem os id's que foram salvos na team.json
        listUser = times_model.id_users
        # percorre a lista
        for user in listUser:
            # busca os dados da tabela users
            usuario = self._usuario_repository.busca_id_usuario(user)
            # insere
            self._usuario_repository.post_usuario(usuario)
=======
        
>>>>>>> origin/develop
    def create_user_team(self,idGroup:int, userTeams:list[user_team_model]):
        for userTeam in userTeams:
            userTeam.id_team = idGroup
            self._userteam_repository.create(userTeam)
<<<<<<< HEAD
=======

    def update_user_team(self, idTeam:int, userTeams:list[user_team_model]):
        self.delete_id_times(idTeam)
        for userTeam in userTeams:
            self._userteam_repository.create(userTeam)

    def delete_user_team(self, idTeam:int):
        allUserProfiles = self._userteam_repository.get_user_teams_by_team_id(idTeam);

        for userProfile in allUserProfiles:
            self._userteam_repository.delete(userProfile.id);
>>>>>>> origin/develop
