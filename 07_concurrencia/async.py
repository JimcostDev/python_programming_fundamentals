"""
# Asyncio (Programación Asíncrona)
    -Mecanismo: Usa un solo hilo con event loop y corrutinas (async/await).
    -Módulo: asyncio.
    -Caso de uso: I/O-bound con muchas operaciones no bloqueantes (ej: servidores web).
"""
import asyncio

async def fetch_data():
    await asyncio.sleep(1)  # Simula una operación I/O
    return "Datos obtenidos"

async def main():
    resultado = await fetch_data()
    print(resultado)

asyncio.run(main())