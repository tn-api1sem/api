from pydantic import BaseModel


class avaliacaoUsuario_model(BaseModel):
    id: int
    rated_user: str | None
    sprint_id: int | None
    rated_by: int | None
    grade1: int | None
    grade2: int | None
    grade3: int | None
    grade4: int | None
    grade5: int | None
    comment: str | None
