from http.client import OK
from fastapi import APIRouter
from ..models.test_model import test_model as TestModel
from ..services.test_service import test_service
from ..services.usuario_services import usuario_services as UsuarioService
router = APIRouter(
    prefix="/api/v1/test",
    tags=["test"],
    responses={404: {"description": "Not found"}},
)

service = test_service()
usuario_services = UsuarioService()

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