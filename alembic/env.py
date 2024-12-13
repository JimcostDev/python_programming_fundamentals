import os
from dotenv import load_dotenv  # Cargar variables desde .env
from logging.config import fileConfig
from sqlalchemy import engine_from_config
from sqlalchemy import pool
from alembic import context

from sqlmodel import SQLModel
from db import engine  # Importa el motor de base de datos desde tu proyecto
from models import *  # Importa todos tus modelos

# Cargar las variables de entorno
load_dotenv()

# Leer la URL de la base de datos desde el archivo .env
DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise ValueError("DATABASE_URL no está definido en el archivo .env")

# Configurar Alembic con la URL obtenida del .env
config = context.config
config.set_main_option("sqlalchemy.url", DATABASE_URL)

# Configuración de logging
fileConfig(config.config_file_name)

# Metadatos de los modelos para las migraciones
target_metadata = SQLModel.metadata

# Configurar las migraciones en línea
def run_migrations_online():
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
        )

        with context.begin_transaction():
            context.run_migrations()

run_migrations_online()
