from fastapi import APIRouter
from app.schemas import User, UserId

router = APIRouter(
    prefix="/user",
    tags= ["Users"]
)

usuarios = []

@router.get('/endpoint1')
def endpoint1():
    return({"mensaje":"Bienvenido!"})

@router.get("/obtenerUsuarios")
def obtenerUsuarios():
    return usuarios

@router.post('/crearUsuario')
def crearUsuario(user:User):
    usuario = user.model_dump() # lo pasa a diccionario
    usuarios.routerend(usuario)
    print(usuarios)
    return {"respuesta":f'Usuario {usuario["nombre"]} creado correctamente'}

@router.get('/obtenerUsuario/{user_id}') #como le pasamos el id por url, entonces podemos usar GET
def obtenerUsuarioPorID(user_id:int):
    for user in usuarios:
        if user_id == user["id"]:
            return {"usuario":user}
    return {"respuesta":"Usuario no encontrado"}

@router.post("/obtenerUsuario2") # si lo pasamos en el body, entonces tiene que si o si ser POST claro.
def obtener_usuario_2(user_id:UserId): 
    for user in usuarios:
        if user_id.id == user["id"]:
            return {"usuario":user}
    return {"respuesta":"Usuario no encontrado"}

@router.delete("/deleteUser/{user_id}")
def deleteUser(user_id:int):
    for index, user in enumerate(usuarios):
        if user["id"] == user_id:
            usuarios.pop(index)
            return {
                "respuesta": "Usuario eliminado correctamente",
                "usuarios": usuarios
            }
    return {"respuesta":"Usuario no encontrado"}

@router.put("/updateUser/{user_id}")
def updateUser(user_id:int, updatedUser:User):
    for index, user in enumerate(usuarios):
        if user["id"] == user_id:
            user["id"] = updatedUser.id
            user["nombre"] = updatedUser.nombre
            return {"mensaje":"usuario actualizado"}
    return {"respuesta":"Usuario no encontrado"}
