from http.client import OK
from fastapi import APIRouter

from src.models.sprints_model import SprintsModel
from src.services.sprint_service import SprintService

router = APIRouter(
    prefix="/api/v1/sprint",
    tags=["sprint"],
    responses={404: {"description": "Not found"}},
)

service = SprintService()

@router.get("/")
def get_all_sprint():
    return service.get();

@router.get("/{id}")
def get_sprint_by_id(id:int):
    return service.get_by_id(id);

@router.post("/")
def create_sprint(model: SprintsModel):
    try:
        service.create(model)
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
    