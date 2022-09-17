from http.client import OK
from fastapi import APIRouter

from ..models.usuario_model import usuario_model
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

@router.get("/{id}")
def id_get_usuario(id:int):
    return usuario_services.buscar_id_usuario(id)

@router.post("/")
def post_usuario(objectToPost:usuario_model):
    usuario_services.post(objectToPost)
    return OK
