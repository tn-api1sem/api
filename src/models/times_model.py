from array import array
from xmlrpc.client import boolean
from pydantic import BaseModel


class times_model(BaseModel):
    id: int | None
    times: str | None
    username: str | None
    id_users: list[int] | None
    team_id:list[int]  | None
    id_profile:list[int]  | None
