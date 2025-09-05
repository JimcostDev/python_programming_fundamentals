def fibonacci(n):
    """
    Calcula el nth número en la secuencia de Fibonacci.

    :param n: El índice del número de Fibonacci que se desea calcular (un entero no negativo).
    :return: El nth número de Fibonacci.

    Ejemplo:
    fibonacci(5) == 5  # Calcula el 5° número de Fibonacci (5 = 3 + 2)
    """

    if n == 0 or n == 1:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)

if __name__ == "__main__":
    try:
       #mostrar la lista de los primeros n números de fibonacci
        n = int(input("Escribe un número entero no negativo: "))
        for i in range(n):
            print(fibonacci(i))
    except ValueError as e:
        print(f"Error: {e}")