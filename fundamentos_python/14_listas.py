numeros = [1, 2, 3, 4]
print(numeros)
print(type(numeros))

tareas = ['limpiar la casa', 'ver el partido']
print(tareas)

tipos = [1, True, 'hola']
print(tipos)

print(numeros[0])
print(tareas[1])
text = 'Hola'
# text[0] = 'W'

tareas[0] = 'ir a la playa'
print(tareas)

tareas[0] = 'lavar los platos'
print(tareas)

print(numeros[:3])
print(True in tipos)
print('hola' in tipos)

# ejemplo practico
frutas = [] # declaracion
frutas = ['cereza', 'uva', 'mango'] #inicializando 1 x 3
print(frutas)
frutas[1] = 'banano'
print(frutas)
frutas[2] = 'papaya'
print(frutas)
frutas.append('kiwi') # agregar un valor a mi lista
print(frutas)
frutas.pop() # eliminar el ultimo valor agregado
print(frutas)

for fruta in frutas:
    print(f'Fruta: {fruta}')
