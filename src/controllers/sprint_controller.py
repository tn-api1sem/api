from http.client import OK
from fastapi import APIRouter

from src.services.avaliacaoUsuario_service import avaliacaoUsuario_service

from ..models.sprints_model import SprintsModel
from ..services.sprint_service import SprintService
from ..services.times_service import times_services as TimesService

router = APIRouter(
    prefix="/api/v1/sprint",
    tags=["sprint"],
    responses={404: {"description": "Not found"}},
)

service = SprintService()
times = TimesService()



@router.get("/")
def get_all_sprint():
    return service.get()

@router.get("/{id}")
def get_sprint_by_id(id:int):
    return service.get_by_id(id);

@router.get("/finished/{user_id}")
def get_sprint_finished(user_id: int):
    teams = times.buscar_times()
    user_teams = []

    for team in teams:
        t = times.buscar_id_times(team.id);
        for timesModel in t.times_model:
            if user_id == timesModel.id_user:
                user_teams.append(team.id)

    a = avaliacaoUsuario_service();
    sprintsRated = a.get_already_rated_sprints(user_id);

    r = service.get_sprint_finished(list(dict.fromkeys(user_teams)), sprintsRated);
    return r;

@router.post("/")
def create_sprint(model: SprintsModel):
    try:
        service.create(model)
        return OK
    except Exception as e:
        return str(e)

@router.post("/createForGroup")
def create_sprint_from_group(model: SprintsModel):
    try:
        service.create_for_group(model)
        return OK
    except Exception as e:
        return str(e)
    
@router.put("/")
def update_sprint(model: SprintsModel):
    try:
        service.update(model)
        return OK
    except Exception as e:
        return str(e)

@router.delete("/{id}")
def delete_sprint(id:int):
    try:
        service.delete(id)
        return OK
    except Exception as e:
        return str(e)
