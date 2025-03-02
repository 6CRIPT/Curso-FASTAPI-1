from sqlalchemy.orm import Session
from app.db import models
from app.schemas import User
from app.db.database import get_db
from fastapi import Depends


def crear_usuario(user:User, db:Session = Depends(get_db)):
    usuario = user.dict() # lo pasa a diccionario
    db_user = models.User(**usuario) # crea un objeto de la clase User con los datos del diccionario
    db.add(db_user) # agrega el objeto a la base de datos
    db.commit()
    db.refresh(db_user)