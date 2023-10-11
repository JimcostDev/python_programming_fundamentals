"""
En Python, un set (conjunto) es una colección desordenada de elementos únicos. 
Esto significa que los elementos en un set no tienen un orden específico y no se pueden duplicar. 
Los sets se utilizan cuando se necesita almacenar elementos únicos y realizar operaciones como
 la unión, la intersección y la diferencia entre conjuntos de manera eficiente.

Puedes crear un set en Python utilizando llaves ({}) o la función predefinida set(). Aquí tienes un ejemplo:
"""
# Crear un set con llaves
frutas = {'manzana', 'naranja', 'plátano', 'manzana'} #no pueden haber elementos repetidos
print(frutas)  # Salida: {'naranja', 'plátano', 'manzana'}

# Crear un set con la función set()
colores = set(['rojo', 'azul', 'verde', 'rojo'])
print(colores)  # Salida: {'rojo', 'verde', 'azul'}

# Crear un set a partir de una tupla 
set_from_tuples = set(('python', 'ruby', 'go', 'rust'))
print(set_from_tuples)

# Crear un set a partir de una lista 
numeros = [1,2,3,1,2,3,4]
set_numbers = set(numeros)
print(set_numbers)

"""
Los sets son útiles para realizar operaciones como la unión, intersección y diferencia entre conjuntos. Ejemplo:
"""
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# Unión de sets
union = set1.union(set2)
print(union)  # Salida: {1, 2, 3, 4, 5, 6, 7, 8}

# Intersección de sets
interseccion = set1.intersection(set2)
print(interseccion)  # Salida: {4, 5}

# Diferencia de sets
diferencia = set1.difference(set2)
print(diferencia)  # Salida: {1, 2, 3}

