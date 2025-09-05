
# Las tuplas son una estructura de datos inmutable que contiene una secuencia ordenada de elementos
# Tupla = (1, 2, 3, 4)

# Los elementos están separados por espacios luego de las comas
# Puede contener cualquier tipo de datos
# Cada posición de la tupla tiene un índice
# Podriamos decir que son solo de lectura

numeros = (1, 2, 3, 5)
strings = ('ronny', 'jimcostdev', 'clau', 'marco', 'jimcostdev')
print(numeros)
print('0 =>', numeros[0])
print('-1 =>', numeros[-1])
print(type(numeros))

print(strings)
print(type(strings))

# CRUD
# numeros.append(10)
# print(numeros)
# numeros[1] = 'change'

print(strings)
print(strings.index('ronny'))
print(strings.count('jimcostdev'))

# # convertir tupla a lista
lista = list(strings)
print(lista)
print(type(lista))

lista[1] = 'barabara'
print(lista)

# convertir lista a tupla
tupla = tuple(lista)
print(tupla)