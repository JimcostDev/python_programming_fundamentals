# Calcular el promedio de tres números

# declaración de variables
numero_a = 0
numero_b = 0
numero_c = 0
promedio = 0.0

# leer datos
numero_a = int(input('Ingrese el valor del primer número: '))
numero_b = int(input('Ingrese el valor del segundo número: '))
numero_c = int(input('Ingrese el valor del tercer número: '))

# calcular promedio
promedio = (numero_a + numero_b + numero_c) / 3

# mostrar resultdo
print(f'El promedio es: {promedio}')
