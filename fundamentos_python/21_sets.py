"""
En Python, un set (conjunto) es una colección desordenada de elementos únicos. 
Esto significa que los elementos en un set no tienen un orden específico y no se pueden duplicar. 
Los sets se utilizan cuando se necesita almacenar elementos únicos y realizar operaciones como
 la unión, la intersección y la diferencia entre conjuntos de manera eficiente.

Puedes crear un set en Python utilizando llaves ({}) o la función predefinida set(). Aquí tienes un ejemplo:
"""

# crear un set con llaves
frutas = {'kiwi', 'naranja', 'mango', 'fresa', 'kiwi'}
print(frutas)

# crear set con la funcion set()
verduras = set(['zanahoria', 'pimiento', 'papa', 'zanahoria'])
print(verduras)

alimentos = {'leche', 'queso', 'yogurt'}
print(alimentos)

# crear set a partir de una tupla
lenguajes = set(('py', 'js', 'go', 'rust'))
print(lenguajes)

# crear set a partir de una lista
numeros = [1, 10, 15, -2, 8]
set_numeros = set(numeros)
print(set_numeros)

# los sets son utiles para realizar operaciones como:
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# union
union_set = set1.union(set2)
print(union_set)

# interseccion
interseccion = set1.intersection(set2)
print(interseccion)

# diferencia
diferencia = set1.difference(set2)
print(diferencia)

# diferencia simetrica
diferencia_simetrica = set1.symmetric_difference(set2)
print(diferencia_simetrica)