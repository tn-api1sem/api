from ftplib import all_errors
from tokenize import group
from ..models.grupo_model import grupo_model
from ..repository.grupo_repository import grupo_repository
from ..repository.times_repository import times_repository


class grupo_services(object):
    _grupo_repository: grupo_repository = grupo_repository()
    _teamsRepository: times_repository = times_repository()

    def __init__(self):
        pass

    def buscar_grupo(self):
        return self._grupo_repository.get()

    def buscar_id_grupo(self, id):
        return self._grupo_repository.busca_id_grupo(id)

    def create(self, model: grupo_model):
        self._grupo_repository.post_grupo(model)
        self.updateTeam(model);
        
    def update(self, model: grupo_model):
        self._grupo_repository.put_grupo(model)

        teams = self._teamsRepository.findTeamByGroup(model.id);
        for team in teams:
            team.id_group = 0;
            self._teamsRepository.update(team);
        
        self.updateTeam(model)

    def updateTeam(self, model: grupo_model):
        allTeams = self._teamsRepository.get();
        for team in allTeams:
            for groupTeam in model.teams:
                if(team.id != groupTeam):
                    continue
                
                team.id_group = model.id;
                self._teamsRepository.update(team)

    def delete_id_grupo(self, id: int):
        allTeams = self._teamsRepository.get();        
        
        for team in allTeams:
            if team.id_group == id:
                raise Exception("Existe um time associado a este grupo, por favor atulize-o antes de excluir");

        return self ._grupo_repository.delete_id_grupo(id)
