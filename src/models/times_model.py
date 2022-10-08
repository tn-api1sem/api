from array import array
from xmlrpc.client import boolean
from pydantic import BaseModel


class times_model(BaseModel):
    times: str
    id_users: list[int]
    id: int
