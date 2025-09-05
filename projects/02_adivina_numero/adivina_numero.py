
"""
adivina el número entre del 1 al 10, suerte.
"""
import random

# Generar un número aleatorio entre 1 y 10
numero_secreto = random.randint(1, 10)

# Función para verificar el número ingresado por el jugador
def verificar_numero(numero):
    if numero == numero_secreto:
        print("¡Felicidades! ¡Adivinaste el número!")
        return True
    elif numero < numero_secreto:
        print("Incorrecto. El número es mayor. Intenta de nuevo.")
    else:
        print("Incorrecto. El número es menor. Intenta de nuevo.")
    return False

# Bucle principal del juego
adivinado = False
while not adivinado:
    try:
        # Leer el número ingresado por el jugador
        numero_ingresado = int(input("Adivina el número (entre 1 y 10): "))
        # Verificar si el número es correcto
        adivinado = verificar_numero(numero_ingresado)
    except ValueError:
        print("Por favor, ingresa un número válido.")

