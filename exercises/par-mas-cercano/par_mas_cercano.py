"""
Autor: Ronaldo Jiménez Acosta
Sitio web: www.jimcostdev.com
Materia: Diseño Avanzado de Algoritmos
Fecha de entrega: 30 de octubre de 2023
"""

import math
import time

def distancia_euclidiana(punto1, punto2):
    """
    Halla la distancia euclidiana entre dos puntos en un plano cartesiano.
    :param punto1: Tupla con las coordenadas (x, y) del primer punto.
    :param punto2: Tupla con las coordenadas (x, y) del segundo punto.
    :return: La distancia euclidiana entre los dos puntos.
    """
    return math.sqrt((punto1[0] - punto2[0]) ** 2 + (punto1[1] - punto2[1]) ** 2)

def encontrar_par_cercano_en_franja(franja, mejor_distancia):
    """
    Encuentra el par de puntos más cercano dentro de una franja vertical.
    :param franja: Lista de puntos dentro de la franja.
    :param mejor_distancia: La mejor distancia encontrada hasta ahora.
    :return: Una tupla con el par de puntos más cercano y la distancia mínima entre ellos en la franja.
    """
    mejor_par = None
    n = len(franja)
    for i in range(n):
        for j in range(i + 1, min(i + 7, n)):
            distancia = distancia_euclidiana(franja[i], franja[j])
            if distancia < mejor_distancia:
                mejor_distancia = distancia
                mejor_par = (franja[i], franja[j])
    return mejor_par, mejor_distancia

def obtener_par_mas_cercano_recursivo(puntos_ordenados_x):
    """
    Función recursiva que divide los puntos en mitades para encontrar el par más cercano.
    :param puntos_ordenados_x: Lista de puntos ordenados por la coordenada x.
    :return: Una tupla con el par de puntos más cercano y la distancia mínima entre ellos.
    """
    n = len(puntos_ordenados_x)
    if n <= 3:
        # Para pocos puntos, calcular la distancia directamente
        min_dist = float('inf')
        par_min = None
        for i in range(n):
            for j in range(i + 1, n):
                dist = distancia_euclidiana(puntos_ordenados_x[i], puntos_ordenados_x[j])
                if dist < min_dist:
                    min_dist = dist
                    par_min = (puntos_ordenados_x[i], puntos_ordenados_x[j])
        return par_min, min_dist

    mitad = n // 2
    mitad_izq = puntos_ordenados_x[:mitad]
    mitad_der = puntos_ordenados_x[mitad:]

    par_izq, distancia_izq = obtener_par_mas_cercano_recursivo(mitad_izq)
    par_der, distancia_der = obtener_par_mas_cercano_recursivo(mitad_der)

    if distancia_izq < distancia_der:
        mejor_par, mejor_distancia = par_izq, distancia_izq
    else:
        mejor_par, mejor_distancia = par_der, distancia_der

    x_mitad = puntos_ordenados_x[mitad][0]
    franja = [punto for punto in puntos_ordenados_x if abs(punto[0] - x_mitad) < mejor_distancia]
    franja.sort(key=lambda punto: punto[1])

    par_franja, distancia_franja = encontrar_par_cercano_en_franja(franja, mejor_distancia)
    if par_franja:
        return par_franja, distancia_franja
    return mejor_par, mejor_distancia

def obtener_par_mas_cercano(puntos):
    """
    Halla el par de puntos más cercano en una lista de puntos utilizando el algoritmo de Divide y Vencerás.
    :param puntos: Lista de puntos en un plano cartesiano.
    :return: Una tupla con el par de puntos más cercano y la distancia mínima entre ellos.
    """
    puntos_ordenados_x = sorted(puntos, key=lambda punto: punto[0])
    return obtener_par_mas_cercano_recursivo(puntos_ordenados_x)

def leer_archivo(archivo):
    """
    Lee un archivo de texto que contiene las coordenadas de los puntos en un formato específico.
    :param archivo: Nombre del archivo de texto que contiene las coordenadas de los puntos.
    :return: Una lista de tuplas con las coordenadas de los puntos.
    """
    puntos = []
    with open(archivo, 'r') as file:
        for linea in file:
            if linea.strip():
                coords = list(map(int, linea.split(',')))
                puntos.extend((coords[i], coords[i + 1]) for i in range(0, len(coords), 2))
    return puntos

def procesar_archivo(archivo):
    """
    Procesa un archivo de puntos, encuentra el par más cercano y mide el tiempo de ejecución.
    :param archivo: Nombre del archivo de texto que contiene las coordenadas de los puntos.
    """
    print(f"Procesando archivo: {archivo}")
    tiempo_inicio = time.time()
    puntos = leer_archivo(archivo)
    par_mas_cercano, distancia_minima = obtener_par_mas_cercano(puntos)
    tiempo_fin = time.time()

    print(f"El par de puntos más cercano es: {par_mas_cercano}")
    print(f"La distancia mínima es: {distancia_minima:.4f}")
    print(f"Tiempo de ejecución: {tiempo_fin - tiempo_inicio:.4f} segundos")
    print()

def main():
    """
    Función principal del programa que procesa tres archivos de puntos y muestra los resultados por separado.
    """
    archivos = ["datos_100.txt", "datos_1000.txt", "datos_10000.txt"]
    for archivo in archivos:
        procesar_archivo(archivo)

if __name__ == '__main__':
    main()
