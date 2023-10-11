"""
FILTER
La función filter(), devuelve un valor que esta siendo iterado de la cual su resultado será el valor que se esta buscando en el filter

SINTAXIS
filter(function, iterable)
"""
# listas 
numbers = [1,2,3,4,5]
pairs = list(filter(lambda x: x % 2 == 0, numbers)) # filtrar los numeros pares
print(pairs)

# dicts
people = [
  {
    'name' : 'Pedro',
    'country': 'Colombia',
    'age' : 18,
    'course' : 'developer'
  },
  {
    'name' : 'Juan',
    'country': 'Perú',
    'age' : 17,
    'course' : 'UX'
  },
  {
    'name' : 'Carlos',
    'country': 'Chile',
    'age' : 31,
    'course' : 'Diseño'
  },
  {
    'name' : 'Ana Maria',
    'country': 'Colombia',
    'age' : 25,
    'course' : 'Tester'
  }
]

# filtrar por pais
countrie = list(filter(lambda country: country['country'] == 'Colombia', people))
print(countrie)

# filtrar si es mayor de edad
adult = list(filter(lambda age: age['age'] >= 18, people))
print(adult)
