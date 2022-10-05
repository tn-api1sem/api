from pydantic import BaseModel

class profile_model(BaseModel):
    usuario:str
    perfil:str
    id_team:int
    id:int

