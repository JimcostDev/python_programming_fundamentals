"""
Métodos de las listas

append(): Añade un ítem al final de la lista.
clear(): Vacía todos los ítems de una lista.
extend(): Une una lista a otra.
count(): Cuenta el número de veces que aparece un ítem.
index(): Devuelve el índice en el que aparece un ítem (error si no aparece).
insert(): Agrega un ítem a la lista en un índice específico.
pop(): Extrae un ítem de la lista y lo borra.
remove(): Borra el primer ítem de la lista cuyo valor concuerde con el que indicamos.
reverse(): Le da la vuelta a la lista actual.
sort(): Ordena automáticamente los ítems de una lista por su valor de menor a mayor.
"""
# CRUD Create, Read, Update & Delete

numeros = [1, 2 , 3 , 4 , 5]
print(numeros[1])
numeros[-1] = 10 # actulizacion de valor
print(numeros)

# agregar valores 
numeros.append(700) # agregar valor al final
print(numeros)

numeros.insert(3, 'hola') # agregar valor indicando un indice
print(numeros)

# concatenar o unir listas
tareas = ['tarea 1', 'tarea 2', 'tarea 3']
nueva_lista = numeros + tareas
print(nueva_lista)

indice = nueva_lista.index('tarea 3') # buscar indice
print(indice)
nueva_lista[indice] = 'tarea nueva 3'
print(nueva_lista)

# eliminar valores
nueva_lista.remove('tarea 1') # por valor
print(nueva_lista)

nueva_lista.pop() # elimina el elemento que esta al final
print(nueva_lista)

nueva_lista.pop(0) # por indice
print(nueva_lista)

nueva_lista.reverse()
print(nueva_lista)

# ordenar lista
numeros_a = [1, 4, 6 , 3]
numeros_a.sort()
print(numeros_a)

strings = ['re', 'ab', 'ed']
strings.sort()
print(strings)

# nueva_lista.sort()