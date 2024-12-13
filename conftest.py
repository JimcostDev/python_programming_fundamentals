import os
import pytest
from fastapi.testclient import TestClient
from sqlmodel import Session, SQLModel, create_engine
from dotenv import load_dotenv

from db import get_session
from app.main import app

# Cargar variables de entorno desde .env
load_dotenv()

# Cadena de conexión para PostgreSQL de pruebas
DATABASE_URL = os.getenv("TEST_DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("DATABASE_URL no está definido en el archivo .env")


# Crear un engine para la base de datos de pruebas
engine = create_engine(DATABASE_URL)

@pytest.fixture(name="session")
def session_fixture():
    """
    Configura una sesión de base de datos para las pruebas. Se utiliza una base de datos de pruebas separada.
    """
    # Crear las tablas en la base de datos de pruebas
    SQLModel.metadata.create_all(engine)
    with Session(engine) as session:
        yield session
    # Opcional: Eliminar las tablas después de las pruebas
    SQLModel.metadata.drop_all(engine)


@pytest.fixture(name="client")
def client_fixture(session: Session):
    """
    Configura un cliente de prueba de FastAPI con una sesión de base de datos de pruebas.
    """
    def get_session_override():
        return session

    # Sobrescribir la dependencia de sesión en la aplicación
    app.dependency_overrides[get_session] = get_session_override
    client = TestClient(app)
    yield client
    # Limpiar las dependencias sobrescritas después de las pruebas
    app.dependency_overrides.clear()
