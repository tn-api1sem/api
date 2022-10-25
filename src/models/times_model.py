from array import array
from xmlrpc.client import boolean
from pydantic import BaseModel


class times_model(BaseModel):
    id: int | None
    times: str | None
    id_users: list[int] | None
