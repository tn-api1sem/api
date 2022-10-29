from pydantic import BaseModel

class user_team_model(BaseModel):
    id:int | None
    id_user:int | None
    id_group:int | None
    id_profile:int | None

class times_bd(BaseModel):
    id: int | None
    times: str | None

class times_model(BaseModel):
    id: int | None
    times: str | None
    times_model: list[user_team_model] | None



