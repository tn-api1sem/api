from http.client import OK
from fastapi import APIRouter

from  ..models.avaliacao_model import avaliacao_model
from ..services.avaliacao_service import avaliacao_services as AvaliacaoService

router = APIRouter(
    prefix="/api/v1/avaliacao",
    tags=["avaliacao"],
    responses={404: {"description": "Not found"}},
)
avaliacao_services = AvaliacaoService()

@router.get("/")
def get_avaliacao():
    return avaliacao_services.get_avaliacao()

@router.get("/{id}")
def get_avaliacao_by_id(id:int):
    return avaliacao_services.get_avaliacao_by_id(id)

@router.post("/")
def create_avaliacao(objectToPost:avaliacao_model):
    avaliacao_services.create(objectToPost)
    return OK

@router.put("/")
def update_avaliacao(objectToPut:avaliacao_model):
    avaliacao_services.update(objectToPut)
    return OK

@router.delete("/{id}")
def delete_id_avaliacao(id:int):
    avaliacao_services.delete(id)
    return OK