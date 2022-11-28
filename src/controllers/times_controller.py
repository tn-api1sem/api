from http.client import BAD_REQUEST,OK
from fastapi import APIRouter

from ..models.times_model import times_model
from ..services.times_service import times_services as TimesService

from  ..models.profile_model import profile_model
from ..services.profile_service import profile_services as ProfileService

router = APIRouter(
    prefix="/api/v1/times",
    tags=["times"],
    responses={404: {"description": "Not found"}},
)
times_services = TimesService()

@router.get("/")
def get_times():
    try:
        return times_services.buscar_times()
    except Exception as e:
        return str(e)


@router.get("/{id}")
def get_time_by_id(id: int):
    return times_services.buscar_id_times(id)


@router.post("/")
def post_times(objectToPost: times_model):
    try:
        times_services.post_times(objectToPost)
        return OK
    except Exception as e:
        return str(e)


@router.put("/")
def put_times(objectToPut: times_model):
    try:
        times_services.put_times(objectToPut)
        return OK
    except Exception as e:
        return str(e)

@router.delete("/{id}")
def delete_id_times(id:int):
    times_services.delete(id)
    return OK
