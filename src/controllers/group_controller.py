from http.client import OK
from fastapi import APIRouter

router = APIRouter(
    prefix="/api/v1/group",
    tags=["group"],
    responses={404: {"description": "Not found"}},
)

@router.get("/")
def get_all():
    return {}

@router.get("/{id}")
def get_by_id(id:int):
    return {}

@router.post("/")
def create():
    return {};

@router.put("/")
def update():
    return {}

@router.delete("/{id}")
def delete_sprint(id:int):
    return {}