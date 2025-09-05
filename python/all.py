"""
La función all() en Python es una herramienta muy útil para verificar 
si todos los elementos de un iterable (como una lista, tupla, conjunto, etc.)
cumplen con una determinada condición, generalmente si son verdaderos.
"""
lista_numeros = [2, 4, 6, 8]
resultado = all(num > 0 for num in lista_numeros)
print(resultado)  # Imprime: True

# Verificar si todos los elementos de una lista son cadenas
lista_palabras = ["hola", "mundo", "Python"]
resultado = all(isinstance(palabra, str) for palabra in lista_palabras)

# Verificar si todos los elementos de un diccionario son mayores que 10
diccionario = {'a': 12, 'b': 15, 'c': 8}
resultado = all(valor > 10 for valor in diccionario.values())