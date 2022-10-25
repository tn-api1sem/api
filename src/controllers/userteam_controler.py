from http.client import OK
from fastapi import APIRouter

from  ..models.userteam_model  import timeProfile_model
from ..services.profile_service import profile_services as ProfileService

router = APIRouter(
    prefix="/api/v1/profile",
    tags=["userteam"],
    responses={404: {"description": "Not found"}},
)
userteam_services = userteamService()


@router.get("/")
def get_profiles():
    return  userteam_services.get_userteam()

@router.get("/{id}")
def get_profile_by_id(id:int):
    return userteam_services.get_userteam_by_id(id)

@router.post("/")
def create_profile(objectToPost:timeProfile_model):
    userteam_services.create(objectToPost)
    return OK

@router.put("/")
def update_userteam(objectToPut:timeProfile_model):
    userteam_services.update(objectToPut)
    return OK

@router.delete("/{id}")
def delete_profile(id:int):
    userteam_services.delete(id)
    return OK

