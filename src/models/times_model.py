from pydantic import BaseModel

class user_team_model(BaseModel):
    id:int | None
    id_user:int | None
    id_team:int | None
    id_profile:int | None
    user: str | None
    profile: str | None

class times_bd(BaseModel):
    id: int | None
    times: str | None
    id_group:int | None

class times_model(BaseModel):
    id: int | None
    times: str | None
    usuarios: str | None
    times_model: list[user_team_model] | None
    




