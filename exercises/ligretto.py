# Simulación del juego de ligretto
# autor: Ronaldo Jiménez - jimcostdev.com

jugadores = {}

# Solicitar el número de jugadores al usuario
num_jugadores = int(input("Ingrese el número de jugadores: "))

# Solicitar los nombres de los jugadores y agregarlos al diccionario
for i in range(num_jugadores):
    nombre = input(f"Ingrese el nombre del jugador {i+1}: ")
    jugadores[nombre] = []

# Función que obtiene el puntaje
def mostrar_puntaje(jugador):
    sumatoria = sum(jugador)
    return sumatoria

# Juego por rondas hasta que un jugador alcance una puntuación de 100
while True:
    for nombre in jugadores.keys():
        puntajes = input(f"Ingrese los puntajes para {nombre} en esta ronda, separados por comas: ")
        puntajes = [int(p) for p in puntajes.split(",")]
        jugadores[nombre].extend(puntajes)

        if mostrar_puntaje(jugadores[nombre]) >= 100:
            print(f"¡El jugador {nombre} ha alcanzado 100 puntos! ¡Fin del juego!")
            exit(0)

    # Imprimir los puntajes de cada jugador después de cada ronda
    for nombre, puntajes in jugadores.items():
        print(f'Puntos {nombre}: {mostrar_puntaje(puntajes)}')
