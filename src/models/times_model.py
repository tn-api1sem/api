from pydantic import BaseModel


class times_model(BaseModel):
    id: int | None
    times: str | None
    username: str | None


class user_team_model(BaseModel):
    id:int
    id_users:int
    team_id:int
    id_profile:int

