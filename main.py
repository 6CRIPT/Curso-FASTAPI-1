from fastapi import FastAPI
import uvicorn
from app.routes.user import router
from app.db.database import Base, engine

def create_tables():
    Base.metadata.create_all(bind=engine)

create_tables()
app = FastAPI()
app.include_router(router) #le metemos el router.

if __name__ == "__main__":
    uvicorn.run("main:app", port = 8000, reload=True)