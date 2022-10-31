from pydantic import BaseModel

class grupo_model(BaseModel):
    name: str
    client_id: int
    leader_id: int
    teams: list [int]

