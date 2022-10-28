from pydantic import BaseModel

class grupo_model(BaseModel):
    usuario: str
    senha: str