from xmlrpc.client import boolean
from pydantic import BaseModel


class userteam_model(BaseModel):
    id: int
    id_users: int
    team_id:int
    id_profile:int

