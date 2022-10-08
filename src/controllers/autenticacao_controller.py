from fastapi import APIRouter
from src.models.login_model import autenticacao_model
from src.services.autenticacao_service import autenticacao_service


router = APIRouter(
    prefix="/api/v1/auth",
    tags=["autenticacao"],
    responses={404: {"description": "Not found"}},
)

service = autenticacao_service()
@router.post("/")
def login (login_model: autenticacao_model):
    return service.login(login_model)

