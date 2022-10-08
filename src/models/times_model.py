from pydantic import BaseModel


class times_model(BaseModel):
    times: str
    id_users: int
    id: int
