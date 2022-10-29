from pydantic import BaseModel

class grupo_model(BaseModel):
    name: str
    client_id: int
    lider_id: int
    times: list [int]

