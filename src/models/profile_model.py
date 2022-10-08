from pydantic import BaseModel

class profile_model(BaseModel):
    usuario:str
    perfil:str
    user_id:int
    profile_id:int

