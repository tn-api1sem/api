from http.client import OK
from fastapi import APIRouter

from  ..models.profile_model import profile_model
from ..services.profile_service import profile_services as ProfileService

router = APIRouter(
    prefix="/api/v1/profile",
    tags=["profile"],
    responses={404: {"description": "Not found"}},
)
profile_services = ProfileService()


@router.get("/")
def get_usuarios():
    return  profile_services.buscar_usuario()

@router.get("/{id}")
def id_get_usuario(id:int):
    return profile_services.buscar_id_usuario(id)

@router.post("/")
def post_usuario(objectToPost:profile_model):
    profile_services.post_profile(objectToPost)
    return OK

def perfil_usuario(objectToPost:profile_model):
    return profile_model

@router.put("/")
def put_usuario(objectToPut:profile_model):
    profile_services.put_profile(objectToPut)
    return OK

@router.delete("/{id}")
def delete_id_usuario(id:int):
    profile_services.delete_id_profile(id)
    return OK

