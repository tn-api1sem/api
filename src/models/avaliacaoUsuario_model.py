from pydantic import BaseModel


class avaliacaoUsuario_model(BaseModel):
    id: int
    rated_user: str | None
    sprint_id: int | None
    rated_by: int | None
    grade: int | None
    comment: str | None
