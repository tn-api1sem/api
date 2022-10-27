from http.client import OK
from fastapi import APIRouter

from src.models.grupo_model import GrupoModel
from src.services.grupo_service import GrupoService

router = APIRouter(
    prefix="/api/v1/grupo",
    tags=["grupo"],
    responses={404: {"description": "Not found"}},
)

service = GrupoService()

@router.get("/")
def get_all_grupo():
    return service.get();

@router.get("/{id}")
def get_grupo_by_id(id:int):
    return service.get_by_id(id);

@router.post("/")
def create_grupo(model: GrupoModel):
    try:
        service.create(model)
        return OK
    except Exception as e:
        return str(e)
    
@router.put("/")
def update_grupo(model: GrupoModel):
    try:
        service.update(model)
        return OK
    except Exception as e:
        return str(e)

@router.delete("/{id}")
def delete_grupo(id:int):
    try:
        service.delete(id)
        return OK
    except Exception as e:
        return str(e)
    