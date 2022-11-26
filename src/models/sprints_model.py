from pydantic import BaseModel


class SprintsModel(BaseModel):
    id: int | None
    name: str | None
    start_date: str | None
    end_date: str | None
    team_id: int | None    
    evaluation_range: str | None

    
