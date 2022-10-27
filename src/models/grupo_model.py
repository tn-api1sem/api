from pydantic import BaseModel

class autenticacao_model(BaseModel):
    usuario: str
    senha: str