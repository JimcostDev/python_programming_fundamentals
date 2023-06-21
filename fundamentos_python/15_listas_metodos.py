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
numeros[-1] = 10
print(numeros)

numeros.append(700)
print(numeros)

numeros.insert(0, 'hola')
print(numeros)

numeros.insert(3, 'change')
print(numeros)

tareas = ['todo 1', 'todo 2', 'todo 3']
nueva_lista = numeros + tareas
print(nueva_lista)

index = nueva_lista.index('todo 2')
nueva_lista[index] = 'todo changed'
print(nueva_lista)

nueva_lista.remove('todo 1')
print(nueva_lista)

nueva_lista.pop()
print(nueva_lista)

nueva_lista.pop(0)
print(nueva_lista)

nueva_lista.reverse()
print(nueva_lista)

numeros_a = [1, 4, 6 , 3]
numeros_a.sort()
print(numeros_a)

strings = ['re', 'ab', 'ed']
strings.sort()
print(strings)

nueva_lista.sort()