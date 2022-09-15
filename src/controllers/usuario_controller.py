from http.client import OK
import json
from fastapi import APIRouter, Response

from ..services.usuario_services import usuario_services as UsuarioService

router = APIRouter(
    prefix="/api/v1/usuario",
    tags=["usuario"],
    responses={404: {"description": "Not found"}},
)
usuario_services = UsuarioService()


@router.get("/")
def get_usuarios():
    return  usuario_services.buscar_usuario()
    