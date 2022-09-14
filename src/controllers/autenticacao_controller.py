from http.client import OK
from fastapi import APIRouter
from pydantic import BaseModel
from src.models.login_model import autenticacao_model
from src.services.autenticacao_service import autenticacao_service

service = autenticacao_service()

router = APIRouter(
    prefix="/api/v1/autenticacao",
    tags=["autenticacao"],
    responses={404: {"description": "Not found"}},
)

@router.post("/")
def login (login_model: autenticacao_model):
    return service.login(login_model)
