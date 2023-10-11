"""
reduce() es una función en Python que se encuentra en el módulo functools. Su objetivo principal es aplicar 
una función a una secuencia de elementos, acumulando el resultado de manera secuencial.
"""

from functools import reduce

numbers = [1, 2, 3, 4]

def accum(counter, item):
  print('counter => ',counter)
  print('item => ',item)
  return counter + item

result = reduce(accum, numbers)
suma = reduce(lambda x, y: x + y, numbers)

print(result)
print(suma)