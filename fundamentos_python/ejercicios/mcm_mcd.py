"""  divisor o factores
20 | 2
10 | 2    2: 2          
5  | 5    5: 1
1

divisor aumentar en 1
"""

"""
10 | 2      2: 1
5  | 5      5: 1
"""
# hallar los factores
def factorizar(numero):
    factores = []
    divisor = 2
    while divisor <= numero:
        if numero % divisor == 0:
            factores.append(divisor) # agregar divisor a lista
            numero = numero // divisor
        else:
            divisor = divisor + 1 # incrementar el divisor porque el modulo no da 0
    return factores

# hallar factores comunes
def obtener_factores_comunes(numeros): #[10, 20]
    factores_comunes = []
    contar_factores = {} # diccionario (llave(numero): valor(factores))
    # obtener factores por cada numero de mi lista numeros
    for num in numeros:
        factores = factorizar(num) 
        contar_factores[num] = {} # ver cuantas veces se repite el factor
        for factor in factores:
            if factor in contar_factores[num]:
                contar_factores[num][factor] += 1
            else:
                contar_factores[num][factor] = 1
            if  factor not in factores_comunes:
                factores_comunes.append(factor)
    return factores_comunes, contar_factores

# hallar mcm
def obtener_mcm(numeros):
    factores_comunes, contar_factores = obtener_factores_comunes(numeros)
    mcm = 1
    for factor in factores_comunes:
        max_conteo = 0
        for num in numeros:
            contar = contar_factores[num].get(factor, 0) # por columa
            if contar > max_conteo:
                max_conteo = contar
        mcm = mcm * factor ** max_conteo
    return mcm

# hallar mcd
def obtener_mcd(numeros):
    factores_comunes, contar_factores = obtener_factores_comunes(numeros)
    mcd = 1
    for factor in factores_comunes:
        min_conteo = min(contar_factores[num].get(factor, 0) for num in numeros)
        mcd = mcd * factor ** min_conteo
    return mcd

# EJECUCION PROGRAMA
numeros = []
cantidad = int(input('¿A cuantos números quieres hallar su mcm y mcd (cantitad)?, digita un valor entre 2 y 10: '))
#validar que la cantidad sea entre 2 y 10
if cantidad >= 2 and cantidad <= 10:
    for number in range(cantidad):
        number = int(input(f'Ingres ael valor del número {number + 1}=> '))
        numeros.append(number) # llenar lista

else:
    print(f'el valor debe estar entre 2 y 10')


# calcular mcm 
mcm = obtener_mcm(numeros)
print(f'El minimo común multiplo(mcm) de {numeros} es: {mcm} ')
# calcular mcd
mcd = obtener_mcd(numeros)
print(f'El máximo común divisor(mcd) de {numeros} es: {mcd} ')

# import math
# mcm_2 = math.lcm(*numeros)
# mcd_2 = math.gcd(*numeros)
# print("MCM", mcm_2)
# print("MCD", mcd_2)

