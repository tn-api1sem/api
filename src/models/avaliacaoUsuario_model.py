from pydantic import BaseModel


class avaliacaoUsuario_model(BaseModel):
    rated_user: str
    sprint_id: int
    rated_by: int
    grade: int
    comment: str
    id: int
