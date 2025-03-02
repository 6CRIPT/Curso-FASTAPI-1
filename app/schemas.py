from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class User(BaseModel):
    id:int
    nombreUsuario:str
    password:str
    nombre:str
    apellido:str
    direccion:Optional[str]
    telefono:int
    correo:str
    creacion_user: datetime = datetime.now()

class UserId(BaseModel):
    id:int

class ShowUser(BaseModel):
    nombreUsuario:str
    nombre:str
    apellido:str
    direccion:Optional[str]
    telefono:int
    correo:str

    class Config: #con esto basicamente consigues simplemente que funcione xd que pydantic aplique el ORM y haga la transformacion como se supone.
        from_attributes = True  # En vez de orm_mode
        
class PatchUser(BaseModel):
    nombreUsuario: Optional[str] = None
    nombre: Optional[str] = None
    apellido: Optional[str] = None
    direccion: Optional[str] = None
    telefono: Optional[int] = None
    correo: Optional[str] = None

    class Config:
        from_attributes = True  # Usar el ORM para mapear los atributos
    