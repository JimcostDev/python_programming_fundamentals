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