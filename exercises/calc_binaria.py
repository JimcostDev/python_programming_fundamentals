
"""
Convertir un numero binario a decimal
"""
binario = input('Ingrese el numero binario: ')
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


print(f'El número en decimal es:  {total}')