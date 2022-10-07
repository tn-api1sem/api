from pydantic import BaseModel


class times_model(BaseModel):
    times: str
    id_times: int
    id: int
