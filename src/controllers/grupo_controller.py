from http.client import OK
from fastapi import APIRouter

from src.models.grupo_model import grupo_model
from src.services.grupo_service import grupo_services as GrupoService

router = APIRouter(
    prefix="/api/v1/grupo",
    tags=["grupo"],
    responses={404: {"description": "Not found"}},
)

grupo_service = GrupoService()

@router.get("/")
def get_all_grupo():
    return grupo_service.buscar_grupo()

@router.get("/{id}")
def get_grupo_by_id(id:int):
    return grupo_service.buscar_id_grupo(id);

@router.post("/")
def create_grupo(model: grupo_model):
    try:
        grupo_service.post_grupo(model)
        return OK
    except Exception as e:
        return str(e)
    
@router.put("/")
def update_grupo(model: grupo_model):
    try:
        grupo_service.put_grupo(model)
        return OK
    except Exception as e:
        return str(e)

@router.delete("/{id}")
def delete_grupo(id:int):
    try:
        grupo_service.delete_id_grupo(id)
        return OK
    except Exception as e:
        return str(e)
    