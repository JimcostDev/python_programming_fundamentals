from fastapi import Depends, FastAPI
from typing import Annotated
from sqlmodel import SQLModel, Session, create_engine
from dotenv import load_dotenv
import os

# Cargar las variables de entorno desde un archivo .env
load_dotenv()

# Obtener la URL de conexión desde las variables de entorno
DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("DATABASE_URL no está definido en el archivo .env")

# Crear el motor de la base de datos usando directamente la cadena de conexión
engine = create_engine(DATABASE_URL)

def create_all_tables(app: FastAPI):
    SQLModel.metadata.create_all(engine)
    yield
    
# Crear una dependencia para obtener una sesión de base de datos
def get_session():
    with Session(engine) as session:
        yield session

# Alias para la dependencia de la sesión
SessionDep = Annotated[Session, Depends(get_session)]
