
from http.client import OK
from fastapi import APIRouter
from  ..models.times_model import times_bd
from ..models.grupo_model import grupo_model
from ..services.grupo_service import grupo_services as GrupoService

router = APIRouter(
    prefix="/api/v1/grupo",
    tags=["grupo"],
    responses={404: {"description": "Not found"}},
)

service = GrupoService()


@router.get("/")
def get_all_grupo():
    return service.buscar_grupo()


@router.get("/{id}")
def get_grupo_by_id(id: int):
    return service.buscar_id_grupo(id)


@router.post("/")
def create_grupo(model: grupo_model):
    try:
        service.create(model)
        return OK
    except Exception as e:
        return str(e)

@router.put("/")
def update_grupo(model: grupo_model):
    try:
        service.update(model)
        return OK
    except Exception as e:
        return str(e)


@router.delete("/{id}")
def delete_grupo(id: int):
    try:
        service.delete_id_grupo(id)
        return OK
    except Exception as e:
        return str(e)