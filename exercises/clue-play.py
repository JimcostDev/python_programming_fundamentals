# juego de adivinanzas con pistas
def mostrar_pista(pista):
    print(f"Pista: {pista}")

def jugar_adivinanza(palabra_secreta, pistas):
    intentos = 3
    adivinado = False

    print("¡Bienvenido al juego de adivinanzas!")
    print("Tienes que adivinar la palabra secreta basada en las pistas que te daremos.")
    print(f"Tienes {intentos} intentos para adivinar la palabra.\n")

    for pista in pistas:
        mostrar_pista(pista)
        respuesta = input("¿Cuál crees que es la palabra secreta? ").strip() # Eliminar espacios en blanco al inicio y al final

        if respuesta.lower() == palabra_secreta.lower():
            print(f"¡Correcto! La palabra secreta es '{palabra_secreta}'.")
            adivinado = True
            break
        else:
            intentos -= 1
            if intentos > 0:
                print(f"Incorrecto. Te quedan {intentos} intentos.\n")
            else:
                print("Lo siento, te has quedado sin intentos.")

    if not adivinado:
        print(f"La palabra secreta era '{palabra_secreta}'. ¡Mejor suerte la próxima vez!")

def main():
    palabra_secreta = "Go"
    pistas = [
        "Es un lenguaje compilado y estáticamente tipado.",
        "Su mascota es un geómido.",
        "Fue desarrollado por Google y su nombre es muy corto.",
    ]

    jugar_adivinanza(palabra_secreta, pistas)

if __name__ == "__main__":
    main()