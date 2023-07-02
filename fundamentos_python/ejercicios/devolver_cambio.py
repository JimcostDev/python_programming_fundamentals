"""
dado el costo de un articulo vendido y la cantidad de dinero
entregada por el cliente, calcule e imprima el cambio que debe entregarse al cliente.
Debe tener en cuenta que para dar el cambio solo puede usar billetes de 10000, 5000 y 2000,
ademas de monedas de 1000, 500, 200, 100, 50. Siempre debe entregar el menor numero 
posible de billtes y monedas.
"""
def calcular_cambio(devuelta):
    billetes = [10000, 5000, 2000, 1000]
    monedas = [500, 200, 100, 50]
    cambio = devuelta
    resultado_billetes = {}
    resultado_monedas = {}

    # Calcula la cantidad de billetes necesarios para el cambio
    for valor in billetes:
        cantidad = cambio // valor # Calcula la división entera para obtener la cantidad de billetes
        if cantidad > 0:
            resultado_billetes[valor] = cantidad # Agrega el valor y la cantidad al diccionario de resultados
            cambio %= valor # Calcula el residuo utilizando el operador de módulo (%)

    # Calcula la cantidad de monedas necesarias para el cambio
    for valor in monedas:
        cantidad = cambio // valor
        if cantidad > 0:
            resultado_monedas[valor] = cantidad
            cambio %= valor

    return resultado_billetes, resultado_monedas

# Ejemplo de uso
valor_producto = int(input('¿Cuanto vale el producto? escriba el valor: '))
valor_pagadoXusuario = int(input('¿Cuanto pago el cliente? escriba el valor: '))
devuelta = valor_pagadoXusuario - valor_producto

if devuelta == 0:
    print('No se debe devolver nada, pago exacto')
else:
    billetes, monedas = calcular_cambio(devuelta)

    print("Cambio a entregar:")
    print("Billetes:")
    for valor, cantidad in billetes.items():
        print(f"{cantidad} de ${valor}")

    print("Monedas:")
    for valor, cantidad in monedas.items():
        print(f"{cantidad} de ${valor}")


# print("EXPLICACIÓN %")
# print(750//500)
# print(750%500)
"""
La operación de módulo % se utiliza para calcular el residuo de cambio que aún queda por entregar 
después de haber utilizado la mayor cantidad posible de billetes o monedas en la iteración actual. 
Por ejemplo, si tenemos un cambio de 750 y estamos utilizando monedas de 500, la división entera 750 // 500 
nos dará 1 (indicando que necesitamos 1 moneda de 500), y el operador de módulo 750 % 500 nos dará 250 
(que es el remanente que aún debemos cubrir con otras denominaciones).
"""