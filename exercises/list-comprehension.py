"""
Las list comprehensions, son una característica poderosa de Python que nos permite crear 
listas de forma concisa y eficiente utilizando una sintaxis compacta. 
Las list comprehensions son una forma elegante de transformar o 
filtrar elementos de una lista existente para crear una nueva lista.

La sintaxis básica de una list comprehension es la siguiente:
"""
# nueva_lista = [expresion for elemento in lista_original if condicion]

"""
* expresion: es una expresión que define cómo se transformarán los elementos de la lista original para obtener los elementos de la nueva lista.
* elemento: es una variable que representa cada elemento de la lista original mientras se recorre.
* lista_original: es la lista de origen de la cual se obtendrán los elementos.
* condicion: es una condición opcional que filtra los elementos de la lista original.
"""

numeros = [1, 2, 3, 4, 5]

# Crear una nueva lista con el cuadrado de los números pares de la lista original
cuadrados_pares = [num ** 2 for num in numeros if num % 2 == 0]
print(cuadrados_pares)  # Output: [4, 16]

# Crear una nueva lista con los números impares multiplicados por 2 de la lista original
impares_multiplicados = [num * 2 for num in numeros if num % 2 != 0]
print(impares_multiplicados)  # Output: [2, 6, 10]

# Crear una nueva lista con los números pares de la lista original, y 'No par' para los impares
numeros_par_o_no_par = ['Par' if num % 2 == 0 else 'No par' for num in numeros]
print(numeros_par_o_no_par)  # Output: ['No par', 'Par', 'No par', 'Par', 'No par']

#SOLUCIÓN RETO:
"""
En este desafío, debes crear la lógica de la función find_words_with_two_vowels que 
encuentre las palabras que contienen exactamente dos vocales en una lista de palabras. 
Las vocales pueden ser tanto mayúsculas como minúsculas.
"""

def tiene_vocal(palabra):
    vocales = "aeiouAEIOU"
    lista_valores = [True if letra in vocales else False for letra in palabra]
    return lista_valores

def contar_vocales(palabra):
    palabra = tiene_vocal(palabra)
    contador_vocales = palabra.count(True)
    return contador_vocales

def find_words_with_two_vowels(words):
    return [word for word in words if contar_vocales(word) == 2]

print(find_words_with_two_vowels([
    "hello",
    "Python",
    "world",
    "platzi"
])
)


