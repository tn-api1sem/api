from array import array
from xmlrpc.client import boolean
from pydantic import BaseModel

class avaliacao_model(BaseModel):

    id: int
    nota: int
    comment: str
