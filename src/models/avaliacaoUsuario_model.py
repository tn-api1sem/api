from array import array
from xmlrpc.client import boolean
from pydantic import BaseModel


class avaliacaoUsuario_model(BaseModel):
    rated_user: str
    rate_id: int
    sprint_id: int
    rated_by: int
    id: int
