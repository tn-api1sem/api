from ftplib import all_errors
from tokenize import group
from ..models.grupo_model import grupo_model,grupo_bd

from ..models.times_model import times_bd
from ..repository.grupo_repository import grupo_repository
from ..repository.times_repository import times_repository
from ..repository.times_repository import times_repository


class grupo_services(object):
    _grupo_repository: grupo_repository = grupo_repository()
    _teamsRepository: times_repository = times_repository()

    def __init__(self):
        pass

    def buscar_grupo(self):
        return self._grupo_repository.get()

    def buscar_id_grupo(self, id):
        grupo = self._grupo_repository.busca_id_grupo(id);
        teams = self._teamsRepository.findTeamByGroup(grupo.id);
        grupoModel = self._bdToModel(grupo, teams)    
        return grupoModel;

    def get_groups_by_leaders_id(self, userId):
        allGroups = self._grupo_repository.get_groups_by_leaders_id(userId)

        returnGroups = []
        for group in allGroups:
            returnGroups.append(self.buscar_id_grupo(group.id))

        return returnGroups

    def create(self, model: grupo_model):
        grupoBd = self._modelToBd(model)
        self._validate(model)

        item = self._grupo_repository.post_grupo(grupoBd)
        model.id = item.id;
        self.updateTeam(model);

    def _validate(self, model):
        for teamId in model.teams:
            teamObject = self._teamsRepository.busca_id_times(teamId)
            
            if teamObject.id_group == model.id:
                continue;

            if (teamObject.id_group != 0 and teamObject.id_group != None):
                group = self.buscar_id_grupo(teamObject.id_group)
                raise Exception("O time "+ teamObject.times + " já está associado ao grupo " + group.name + ", por favor retire a relação antes de atribui-lo de novo.")

    def update(self, model: grupo_model):
        grupoBd = self._modelToBd(model)
        self._validate(model);

        self._grupo_repository.put_grupo(grupoBd)
        teams = self._teamsRepository.findTeamByGroup(model.id);
        for team in teams:
            if team.id_group != model.id:
                continue;
                
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


    def _modelToBd(self, model):
        grupoBd = grupo_bd();
        grupoBd.client_id = model.client_id;
        grupoBd.leader_id = model.leader_id;
        grupoBd.id = model.id;
        grupoBd.name = model.name;
        return grupoBd

    def _bdToModel(self, g, teams):
        grupoModel = grupo_model()
        grupoModel.id = g.id
        grupoModel.name = g.name
        grupoModel.client_id = g.client_id
        grupoModel.leader_id = g.leader_id
        grupoModel.teams = list(map(lambda x: x.id, teams))
        return grupoModel;
