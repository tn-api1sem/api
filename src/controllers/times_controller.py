from http.client import OK
from fastapi import APIRouter

from ..models.times_model import times_model
from ..services.times_services import times_services as TimesService

router = APIRouter(
    prefix="/api/v1/times",
    tags=["times"],
    responses={404: {"description": "Not found"}},
)
times_services = TimesService()

@router.get("/")
def get_times():
    return times_services.buscar_times()

@router.get("/{id}")
def id_get_times(id_times:int):
    return times_services.buscar_id_times(id_times)

@router.post("/")
def post_times(objectToPost:times_model):
    times_services.post_times(objectToPost)
    return OK

@router.put("/")
def put_times(objectToPut:times_model):
    times_services.put_times(objectToPut)
    return OK

@router.delete("/{id}")
def delete_id_times(id_times:int):
    times_services.delete_id_times(id_times)
    return OK