from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL") # get the database url from the .env file
engine = create_engine(SQLALCHEMY_DATABASE_URL) # connect to the database
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) # create a session
Base = declarative_base() # create a base class, nos va a servir para crear los modelos.

def get_db(): # devuelve la sesion de la base de datos.
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

