def factorial(number):
    """
    Calcula el factorial de un número entero no negativo.

    :param number: Número al que se le calculará el factorial (debe ser un entero no negativo).
    :return: El factorial del número.

    Ejemplo:
    factorial(5) == 120  # Calcula 5! = 5 * 4 * 3 * 2 * 1
    """

    if number < 0:
        raise ValueError("El número debe ser un entero no negativo")
    elif number == 0:
        return 1
    else:
        return number * factorial(number - 1)


if __name__ == "__main__":
    try:
        number = int(input("Escribe un número entero no negativo: "))
        result = factorial(number)
        print(f"El factorial de {number} es {result}")
    except ValueError as e:
        print(f"Error: {e}")
