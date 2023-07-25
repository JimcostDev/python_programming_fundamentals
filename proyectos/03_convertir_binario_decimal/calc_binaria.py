
"""
Convertir un numero binario a decimal
"""
def calcular_decimal(binario):
    bits = list(binario) #convertir string a lista 
    #convertir elementos de la lista  a enteros
    for bit in range(len(bits)):
        bits[bit] = int(bits[bit])

    #convertir binario a decimal
    total = 0
    acumulador = 1
    bits.reverse() # se invirte el numero para poder realizar el calculo correctamente
    for bit in range(len(bits)):
        acumulador = acumulador *2 # hace de exponente 
        bits[bit] = bits[bit] * acumulador//2
        total += bits[bit]; #sumar los elementos que contiene el vector
    return total

def mostrar_resultado():
    binario = input('Ingrese el numero binario: ')
    # Verificar que solo se ingresen 0 y 1
    if not all(bit in ('0', '1') for bit in binario):
       print ("¡Error! Ingresa solo valores binarios (0 y 1).")
    else:
        numero_binario = calcular_decimal(binario)
        print(f'El número en decimal es:  {numero_binario}')

# ejecutar programa
mostrar_resultado()