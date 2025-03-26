"""
# Multiprocessing (Procesos)
    -Mecanismo: Usa procesos separados (no comparten memoria).
    -Módulo: multiprocessing.
    -Caso de uso: Tareas CPU-bound (ej: cálculos matemáticos intensivos).
    -Ventaja: Evita el GIL al usar múltiples intérpretes.
"""
from multiprocessing import Process

def calcular_cuadrado(n):
    print(f"El cuadrado de {n} es {n * n}")

if __name__ == "__main__":  
    procesos = []
    numeros = [1, 2, 3, 4, 5]

    for num in numeros:
        p = Process(target=calcular_cuadrado, args=(num,))
        procesos.append(p)
        p.start()

    for p in procesos:
        p.join()

    print("Todos los procesos han terminado")