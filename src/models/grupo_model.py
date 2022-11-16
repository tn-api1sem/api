from pydantic import BaseModel


class grupo_model(BaseModel):
    id: int  | None
    name: str | None
    client_id: int | None
    leader_id: int | None
    teams: list[int] | None

class grupo_bd (BaseModel):
    id: int | None
    name: str | None
    client_id: int | None
    leader_id: int | None
    
