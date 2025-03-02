from fastapi import APIRouter
from app.schemas import PatchUser, ShowUser, User, UserId
from app.db.database import get_db #funcion para abrir la base de datos.
from fastapi import Depends # para poder usar la funcion get_db
from sqlalchemy.orm import Session # para poder usar la funcion get_db
from app.db import models
from typing import List
from app.repository import userRepo

router = APIRouter(
    prefix="/user",
    tags= ["Users"]
)

usuarios = []

@router.get('/endpoint1')
def endpoint1():
    return({"mensaje":"Bienvenido!"})

@router.get("/obtenerUsuarios", response_model=List[ShowUser]) # response_model es para que devuelva un json con los datos del usuario.
def obtenerUsuarios(db:Session = Depends(get_db)): # la funcion get_db nos devuelve la sesion de la base de datos.
    return db.query(models.User).all() # esto es para obtener todos los usuarios de la base de datos.


@router.post('/crearUsuario')
def crearUsuario(usuario:User, db:Session = Depends(get_db)):
    userRepo.crear_usuario(usuario, db)
    return {"respuesta":f'Usuario {usuario.nombre} creado correctamente'}

@router.get('/obtenerUsuario/{user_id}', response_model= ShowUser) #como le pasamos el id por url, entonces podemos usar GET
def obtenerUsuarioPorID(user_id: int, db: Session = Depends(get_db)):
    usuario = db.query(models.User).filter(models.User.id == user_id).first()
    if usuario:
        # Usamos model_validate en vez de from_orm
        return ShowUser.model_validate(usuario)  
    return {"respuesta": "Usuario no encontrado"}


@router.post("/obtenerUsuario2") # si lo pasamos en el body, entonces tiene que si o si ser POST claro.
def obtener_usuario_2(user_id:UserId): 
    for user in usuarios:
        if user_id.id == user["id"]:
            return {"usuario":user}
    return {"respuesta":"Usuario no encontrado"}

@router.delete("/deleteUser/{user_id}")
def deleteUser(user_id:int, db:Session = Depends(get_db)):
    usuario = db.query(models.User).filter(models.User.id == user_id).first()
    if not usuario:
        return {"respuesta":"Usuario no encontrado"}
    db.delete(usuario)
    db.commit()
    return {"mensaje":"Usuario eliminado"}

@router.patch("/updateUser/{user_id}")
def updateUser(user_id:int, patch_user:PatchUser, db:Session = Depends(get_db)):
    usuario = db.query(models.User).filter(models.User.id == user_id).first()
    if not usuario:
        return {"respuesta":"Usuario no encontrado"}
    usuario_data = patch_user.model_dump()
    for key, value in usuario_data.items():
        if value is not None:
            setattr(usuario, key, value)
    db.commit()
    return {"mensaje":"Usuario actualizado"}
