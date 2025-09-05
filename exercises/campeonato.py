"""
Este script genera un calendario de partidos (fixture) para una liga utilizando 
el método round-robin, donde todos los equipos se enfrentan entre sí una vez.
Si el número de equipos es impar, se añade un equipo ficticio llamado "Descansa"
para garantizar que cada equipo tenga un oponente en cada jornada.

El algoritmo implementa una variante del método de rotación de Berger, que 
organiza los emparejamientos mediante rotaciones sucesivas de los equipos 
(excepto el primero) para formar nuevas jornadas sin repeticiones.
"""

# Lista de equipos participantes en el torneo
participantes = [
    "Liverpool", 
    "Manchester City", 
    "Tottenham Hotspur",
    "Chelsea",
    "Arsenal",
    "Aston Villa"
]

# Función que genera el calendario (fixture) de enfrentamientos entre los equipos
def sorteo(participantes):
    # Si hay un número impar de equipos, se añade un equipo ficticio "Descansa"
    # para que todos puedan emparejarse en cada jornada.
    if (len(participantes) % 2 != 0):
        participantes.append("Descansa")
        
    fixture = []  # Lista que almacenará todas las jornadas con sus partidos
    rivales = len(participantes) - 1  # Número de jornadas (número de rivales)
    partidos = len(participantes) // 2  # Número de partidos por jornada

    # Generar todas las jornadas
    for r in range(rivales):
        fixture.append([])  # Añadir una nueva jornada vacía
        for p in range(partidos):
            # Emparejar equipos: el primero con el último, el segundo con el penúltimo, etc.
            fixture[r].append((participantes[p], participantes[rivales - p]))
        # Rotación de los equipos (excepto el primero) para generar nuevos enfrentamientos
        participantes.insert(1, participantes.pop())
    
    return fixture  

# Ejecutar la función de sorteo y guardar el resultado
juegos = sorteo(participantes)

# Imprimir el calendario jornada por jornada
for i, juego in enumerate(juegos):
    print(f"Jornada {i+1}")
    for p in juego:
        print(f"{p[0]} vs {p[1]}")
    print()  
