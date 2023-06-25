def calcular(operacion, num1, num2):
    switcher = {
        'suma': num1 + num2,
        'resta': num1 - num2,
        'multiplicacion': num1 * num2,
        'division': num1 / num2
    }
    return switcher.get(operacion, 'Operación inválida')

# Ejemplo de uso
operacion = input("Ingrese la operación (suma, resta, multiplicacion, division): ")
numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))

resultado = calcular(operacion, numero1, numero2)
print("El resultado es:", resultado)