# listas
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

