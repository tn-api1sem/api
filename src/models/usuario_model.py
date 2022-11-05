from pydantic import BaseModel

class usuario_model(BaseModel):
    id:int | None
    email:str | None
    usuario:str | None
    senha:str | None
    



