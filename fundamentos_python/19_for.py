"""
for elemento in range(1, 11):
    print(elemento)
"""

#iterar sobre una lista
print('iterar sobre una lista: ')
numeros = [1, 2, 3, 4]
for numero in numeros:
    print(numero)

#iterar sobre una tupla
print('iterar sobre una tupla: ')
langs = ('py', 'js', 'go')
for lang in langs:
    print(lang)

#iterar sobre un diccionario
print('iterar sobre un diccionario: ')
producto = {
  'name': 'Camisa',
  'price': 100,
  'stock': 45
}
for clave, valor in producto.items():
    print(f'{clave} => {valor}')

# algo muy comun es tener una lista y dentro diccionarios
print()
people = [
  {
    'name': 'nico',
    'age': 34
  },
  {
    'name': 'zule',
    'age': 45
  },
  {
    'name': 'santi',
    'age': 4
  }
]

for person in people:
  print(person)
  print('name =>', person['name'])


# ejercico: crear una lista de numeros y retornar el doble de esos numeros