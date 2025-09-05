"""
Módulo para resolver el puzzle de las losetas.

Este módulo proporciona una implementación para resolver el puzzle de las losetas
utilizando el algoritmo A*. Permite resolver puzzles de tamaños 2x2, 3x3 y 4x4,
determinando si el puzzle tiene solución, mostrando los pasos necesarios para resolverlo
y el tiempo tomado para encontrar la solución.

Autor: Ronaldo Jiménez	
Website: https://jimcostdev.com/

Estructura del Código:
- Clase Puzzle: Encapsula la lógica para resolver el puzzle.
- Funciones Auxiliares: Mostrar Menú y Obtener Tablero.

El algoritmo utiliza la distancia de Manhattan como heurística y verifica la resolubilidad
del puzzle antes de intentar resolverlo.

"""
import heapq
import time
from typing import List, Tuple, Optional

class Puzzle:
    def __init__(self, tablero: List[List[int]]):
        self.tablero = tablero
        self.size = len(tablero)
        self.meta = self.generar_meta()
    
    def generar_meta(self) -> List[List[int]]:
        """Genera el estado meta del puzzle."""
        meta = [[(i * self.size + j + 1) % (self.size * self.size) for j in range(self.size)] for i in range(self.size)]
        return meta

    def encontrar_vacio(self) -> Tuple[int, int]:
        """Encuentra la posición de la loseta vacía (0)."""
        for i in range(self.size):
            for j in range(self.size):
                if self.tablero[i][j] == 0:
                    return i, j

    def es_resoluble(self) -> bool:
        """Determina si el puzzle es resoluble."""
        plano = [num for fila in self.tablero for num in fila]
        inversiones = 0
        fila_vacio = self.encontrar_vacio()[0]
        for i in range(len(plano)):
            for j in range(i + 1, len(plano)):
                if plano[i] != 0 and plano[j] != 0 and plano[i] > plano[j]:
                    inversiones += 1
        if self.size % 2 == 1:
            return inversiones % 2 == 0
        else:
            return (inversiones + fila_vacio) % 2 == 1

    def heuristica(self, tablero: List[List[int]]) -> int:
        """Calcula la distancia de Manhattan desde el estado actual hasta la meta."""
        distancia = 0
        for i in range(self.size):
            for j in range(self.size):
                if tablero[i][j] != 0:
                    meta_x = (tablero[i][j] - 1) // self.size
                    meta_y = (tablero[i][j] - 1) % self.size
                    distancia += abs(i - meta_x) + abs(j - meta_y)
        return distancia

    def obtener_vecinos(self, tablero: List[List[int]]) -> List[Tuple[List[List[int]], str]]:
        """Genera los estados vecinos al mover la loseta vacía en las cuatro direcciones posibles."""
        vecinos = []
        vacio_x, vacio_y = self.encontrar_vacio()
        direcciones = {
            "ARRIBA": (vacio_x - 1, vacio_y),
            "ABAJO": (vacio_x + 1, vacio_y),
            "IZQUIERDA": (vacio_x, vacio_y - 1),
            "DERECHA": (vacio_x, vacio_y + 1)
        }
        for movimiento, (nuevo_x, nuevo_y) in direcciones.items():
            if 0 <= nuevo_x < self.size and 0 <= nuevo_y < self.size:
                nuevo_tablero = [fila[:] for fila in tablero]
                nuevo_tablero[vacio_x][vacio_y], nuevo_tablero[nuevo_x][nuevo_y] = nuevo_tablero[nuevo_x][nuevo_y], nuevo_tablero[vacio_x][vacio_y]
                vecinos.append((nuevo_tablero, movimiento))
        return vecinos

    def resolver(self) -> Tuple[Optional[List[str]], float, str]:
        """Resuelve el puzzle utilizando el algoritmo A*."""
        if not self.es_resoluble():
            return None, 0.0, "No es alcanzable debido a que el número de inversiones indica que es irresoluble."

        inicio_tiempo = time.time()
        tablero_inicio = self.tablero
        tablero_meta = self.meta

        frontera = []
        heapq.heappush(frontera, (0, tablero_inicio, []))
        explorado = set()
        explorado.add(tuple(map(tuple, tablero_inicio)))

        while frontera:
            _, tablero_actual, camino = heapq.heappop(frontera)
            if tablero_actual == tablero_meta:
                fin_tiempo = time.time()
                return camino, fin_tiempo - inicio_tiempo, "Solución encontrada"

            for vecino, movimiento in self.obtener_vecinos(tablero_actual):
                vecino_tuple = tuple(map(tuple, vecino))
                if vecino_tuple not in explorado:
                    explorado.add(vecino_tuple)
                    nuevo_camino = camino + [movimiento]
                    heapq.heappush(frontera, (len(nuevo_camino) + self.heuristica(vecino), vecino, nuevo_camino))

        fin_tiempo = time.time()
        return None, fin_tiempo - inicio_tiempo, "No hay solución alcanzable"

def mostrar_menu() -> int:
    while True:
        print("Seleccione el tamaño del puzzle que desea resolver:")
        print("1. Puzzle 2x2")
        print("2. Puzzle 3x3")
        print("3. Puzzle 4x4")
        try:
            opcion = int(input("Ingrese el número de su opción: "))
            if opcion in [1, 2, 3]:
                return {1: 2, 2: 3, 3: 4}[opcion]
            else:
                print("Opción no válida. Inténtelo de nuevo.")
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número.")

def obtener_tablero(size: int) -> List[List[int]]:
    tablero = []
    for i in range(size):
        while True:
            try:
                fila = list(map(int, input(f"Ingrese la fila {i + 1} de {size}, separando los números con espacios: ").split()))
                if len(fila) == size:
                    tablero.append(fila)
                    break
                else:
                    print(f"Debe ingresar exactamente {size} números.")
            except ValueError:
                print("Entrada no válida. Asegúrese de ingresar números enteros separados por espacios.")
    return tablero

if __name__ == "__main__":
    size_puzzle = mostrar_menu()
    tablero_inicial = obtener_tablero(size_puzzle)

    puzzle = Puzzle(tablero_inicial)
    solucion, tiempo_transcurrido, mensaje = puzzle.resolver()

    if solucion is not None:
        print(f"{mensaje} en {tiempo_transcurrido:.4f} segundos")
        print("Pasos para resolver el puzzle:")
        for paso in solucion:
            print(paso)
    else:
        print(f"{mensaje}.")
