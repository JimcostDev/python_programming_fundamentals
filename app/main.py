from importlib import import_module
from typing import Annotated
from fastapi import Depends, FastAPI, HTTPException, Request, status
from pathlib import Path
from datetime import datetime
import time
import zoneinfo

from fastapi.security import HTTPBasic, HTTPBasicCredentials
from db import create_all_tables


app = FastAPI(
    title="Aprendiendo FastAPI",
    description="Este es un proyecto de ejemplo para aprender FastAPI, SQLModel y otros conceptos.",
    version="0.1.0",
    lifespan=create_all_tables
    )

@app.middleware("http")
async def log_request_time(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    print(f"Request: {request.url} completed in: {process_time:.4f} seconds")

    return response

@app.middleware("http") 
async def log_request_headers(request: Request, call_next):
    
    print("Request Headers:")
    for header, value in request.headers.items():
        print(f"{header}: {value}")

    response = await call_next(request) 

    return response

security = HTTPBasic()
# Ruta principal - Hola, Mundo!
@app.get("/")
async def root(credentials: Annotated[HTTPBasicCredentials,Depends(security)]):
    print(credentials)
    if credentials.username == "jimcostdev" and credentials.password == "12345678":
        return {"message": f"Hola, {credentials.username}!"}
    else:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Credenciales inválidas")


country_timezones = {
    "CO": "America/Bogota",
    "MX": "America/Mexico_City",
    "AR": "America/Argentina/Buenos_Aires",
    "BR": "America/Sao_Paulo",
    "PE": "America/Lima",
    "ES": "Europe/Madrid"
}

## Ejercicio 1 - Crear una ruta que devuelva la fecha y hora actual
@app.get("/datetime/{iso_code}")
async def datetime_now(iso_code: str):
    iso = iso_code.upper()
    timezone_str = country_timezones.get(iso)
    tz = zoneinfo.ZoneInfo(timezone_str)
    return {"datetime": datetime.now(tz).strftime("%Y-%m-%d %H:%M:%S")}

# Función para cargar rutas dinámicamente
def load_routes(app: FastAPI):
    # Ruta para la carpeta de routers
    routes_directory = Path(__file__).parent / "routers"

    # Iterar sobre los archivos .py en la carpeta routers
    for route_file in routes_directory.glob("*.py"):
        if route_file.name != "__init__.py":
            module_name = f"app.routers.{route_file.stem}"  # Namespace completo
            module = import_module(module_name)  # Importar dinámicamente el módulo
            if hasattr(module, "router"):  # Verificar que tenga un router
                app.include_router(module.router)
            else:
                print(f"El módulo {module_name} no tiene un objeto 'router'.")

# Cargar rutas
load_routes(app)






