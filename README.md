## Notas de Alembic para crear migraciones:

### 1. Crea una nueva migración:
```sh
alembic revision --autogenerate -m "Initial migration"
```
### 2. Aplica la migración para actualizar la base de datos:
```sh
alembic upgrade head
```