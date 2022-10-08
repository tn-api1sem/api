from xmlrpc.client import boolean
from pydantic import BaseModel


class times_model(BaseModel):
    times: str
    id_users: int
    id: int
    fl_single: boolean
