"""
# Threads (Hilos)
    -Mecanismo: Usa hilos del sistema operativo (comparten memoria).
    -Módulo: threading.
    -Caso de uso: Tareas I/O-bound (ej: descargas, APIs, lectura de archivos).
    -Limitación: El GIL (Global Interpreter Lock) evita paralelismo real en CPU-bound.
"""
import threading

def tarea():
    print("Hilo ejecutándose")

hilo = threading.Thread(target=tarea)
hilo.start()
hilo.join()