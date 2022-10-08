from pydantic import BaseModel

class usuario_model(BaseModel):
    id:int | None
    id_perfil:int | None
    email:str | None
    usuario:str | None
    senha:str | None
    celular:str | None
    



