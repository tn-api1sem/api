from pydantic import BaseModel

class perfil_model(BaseModel):
    usuario:str
    perfil:str
    id_team:int
    id:int

