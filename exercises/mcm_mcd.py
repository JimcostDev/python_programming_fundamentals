"""
descomponer un número en sus factores primos(2,3,5,7,11,13)
12|2 
6 |2
3 |3
1 |

45|3 
15|3
5 |5
1 |

mcm = 2^2*3^2*5 = 180
mcd = 3^1 = 3
"""
# Esta función toma un número y nos devuelve una lista de sus factores primos. 
def factorizar(num):
    factores = []
    divisor = 2
    while divisor <= num:
        if num % divisor == 0:
            factores.append(divisor)
            num //= divisor
        else:
            divisor += 1
    return factores

#Toma una lista de números y utiliza la función factorizar(num) para obtener los factores primos de cada número. Luego, guarda el conteo de estos factores en un diccionario llamado conteo_factores.
def obtener_factores_comunes(numeros):
    factores_comunes = []
    conteo_factores = {}
    for num in numeros:
        factores = factorizar(num)
        conteo_factores[num] = {}
        for factor in factores:
            if factor in conteo_factores[num]:
                conteo_factores[num][factor] += 1
            else:
                conteo_factores[num][factor] = 1
            if factor not in factores_comunes:
                factores_comunes.append(factor)
    return factores_comunes, conteo_factores

#Utiliza la función obtener_factores_comunes(numeros) para obtener los factores comunes y sus conteos. Luego, con estos datos, calcula el MCM utilizando la fórmula que multiplica los factores elevados a sus conteos máximos.
def obtener_mcm(numeros):
    factores_comunes, conteo_factores = obtener_factores_comunes(numeros)
    mcm = 1
    for factor in factores_comunes:
        max_conteo = 0
        for num in numeros:
            conteo = conteo_factores[num].get(factor, 0)
            if conteo > max_conteo:
                max_conteo = conteo
        mcm = mcm * factor ** max_conteo
    return mcm

#Trabaja de manera similar, calcula el MCD usando la fórmula que multiplica los factores elevados a sus conteos mínimos.
def obtener_mcd(numeros):
    factores_comunes, conteo_factores = obtener_factores_comunes(numeros)
    mcd = 1
    for factor in factores_comunes:
        min_conteo = min(conteo_factores[num].get(factor, 0) for num in numeros)
        mcd = mcd * factor ** min_conteo
    return mcd

# ENTRY POINT
if __name__ == "__main__":
    # Ingresar los números
    numeros = []
    cantidad = int(input('''¿A cuántos números vamos a calcular su mcm y MCD (cantidad)?, digita un valor entre 2 y 10 => '''))
    
    # Validar que la cantidad sea >= 2 y <= 10
    if cantidad >= 2 and cantidad <= 10:
        for x in range(cantidad):
            numero = int(input(f'Ingresa valor de número {x + 1}: '))
            numeros.append(numero)  # Agregar números a la lista
    else:
        print('El valor debe estar entre 2 y 10')

    # Calcular el mínimo común múltiplo (mcm)
    mcm = obtener_mcm(numeros)
    print("El mínimo común múltiplo (mcm) de", numeros, "es:", mcm)

    # Calcular el máximo común divisor (MCD)
    mcd = obtener_mcd(numeros)
    print("El máximo común divisor (MCD) de", numeros, "es:", mcd)


# import math
# numeros = [12,45]
# mcm = math.lcm(*numeros)
# mcd = math.gcd(*numeros)

# print("MCM:", mcm)
# print("MCD:", mcd)