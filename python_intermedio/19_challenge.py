"""
Para resolver este desafío, tu reto es usar la función filter de Python y una función lambda para filtrar una lista de palabras, retornando una lista solo con las que cumplan con la condición de tener 4 o más letras.

La función filter_by_length recibirá como entrada una lista con palabras. Finalmente, la función retornará la lista filtrada.

Input: ['amor', 'sol', 'piedra', 'día']
Output: [ 'amor', 'piedra' ]
"""
def filter_by_length(words):
   # Escribe tu solución 👇
   words_4letters = list(filter(lambda word: len(word) >= 4, words))
   return words_4letters

words = ['amor', 'sol', 'piedra', 'día']
response = filter_by_length(words)
print(response)