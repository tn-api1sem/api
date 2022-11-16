from http.client import OK
from fastapi import APIRouter

from src.models.avaliacaoUsuario_model import avaliacaoUsuario_model
from src.services.avaliacaoUsuario_service import avaliacaoUsuario_service

router = APIRouter(
    prefix="/api/v1/avaliacaoUsuario",
    tags=["avaliacaoUsuario"],
    responses={404: {"description": "Not found"}},
)

service = avaliacaoUsuario_service()


@router.get("/")
def get_avaliacaoUsuario():
    return service.buscar_avaliacaoUsuario()


@router.get("/{id}")
def id_get_avaliacaoUsuario(id: int):
    return service.buscar_id_avaliacaoUsuario(id)


@router.post("/")
def post_avaliacaoUsuario(avaliacaoList: list[avaliacaoUsuario_model]):
    try:
        for avaliacao in avaliacaoList:
            service.post_avaliacaoUsuario(avaliacao)
        return OK
    except Exception as e:
        return str(e)

@router.delete("/{id}")
def delete_id_avaliacaoUsuario(id: int):
    try:
        service.delete_id_avaliacaoUsuario(id)
        return OK
    except Exception as e:
        return str(e)
