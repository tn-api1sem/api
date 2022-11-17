from pydantic import BaseModel


class SprintsModel(BaseModel):
    id: int
    name: str
    start_date: str
    end_date: str
    team_id: int
    evaluation_range: str