# diccionario = {}
# for x in range(1, 6):
#     diccionario[x] = 'valor ' + str(x)

# print(diccionario)

# # DICT COMPREHENSION
# dicc = {x: 'VALOR ' + str(x) for x in range(1, 6)}
# print(dicc)

import random
paises = ['col', 'ven', 'ecu', 'pe']
poblacion = {}

for pais in paises:
    poblacion[pais] = random.randint(1, 100)

print(poblacion)

poblacion_2 = {pais: random.randint(1, 100) for pais in paises}
print(poblacion)
