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
def get_profiles():
    return  profile_services.get_profile()

@router.get("/{id}")
def get_profile_by_id(id:int):
    return profile_services.get_profile_by_id(id)

@router.post("/")
def create_profile(objectToPost:profile_model):
    profile_services.create(objectToPost)
    return OK

@router.put("/")
def update_profile(objectToPut:profile_model):
    profile_services.update(objectToPut)
    return OK

@router.delete("/{id}")
def delete_profile(id:int):
    profile_services.delete(id)
    return OK

