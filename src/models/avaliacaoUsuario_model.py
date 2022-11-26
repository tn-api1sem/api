from pydantic import BaseModel


class avaliacaoUsuario_model(BaseModel):
    id: int | None
    rated_user: str | None
    sprint_id: int | None
    rated_by: int | None
    grade01: int | None
    grade02: int | None
    grade03: int | None
    grade04: int | None
    grade05: int | None
    comment: str | None
