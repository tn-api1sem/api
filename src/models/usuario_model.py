from pydantic import BaseModel

class usuario_model(BaseModel):
    usuario:str
    senha:str
    id_perfil:int
    id:int

