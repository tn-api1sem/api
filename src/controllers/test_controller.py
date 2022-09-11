from http.client import OK
from fastapi import APIRouter
from pydantic import BaseModel
from ..services.test_service import test_service as TestService
from ..models.test_model import test_model as TestModel
 
router = APIRouter(
    prefix="/api/v1/test",
    tags=["test"],
    responses={404: {"description": "Not found"}},
)

service = TestService()

@router.get("/")
def test_getall_route():
    return service.get();

@router.get("/{id}")
def test_get_route(id:int):
    return service.get_by_id(id);

@router.post("/")
def test_post_route(testObject: TestModel):
    service.post(testObject)
    return OK;

@router.put("/")
def test_put_route(testObject: TestModel):
    service.put(testObject)
    return OK

@router.delete("/{id}")
def test_delete_route(id:int):
    service.delete(id)
    return OK