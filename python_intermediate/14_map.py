
"""
# tranformaciones a una lista dada de elementos (como una lista, tupla o conjunto) 
# genera un nuevo iterable que contiene los resultados de aplicar esa función a cada elemento 
# correspondiente del iterable original.
"""
# map(func, iterable)

# EJEMPLO 1

# Creamos una lista de números
numeros = [1, 2, 3, 4, 5]

# Usamos map para aplicar la función duplicar a cada elemento de la lista
resultado = map(lambda x: x * 2, numeros)

# Convertimos el resultado en una lista para ver los valores
resultado_lista = list(resultado)
print(resultado_lista)


# EJEMPLO 2
def cocinar(ingrediente):
    if  ingrediente == '🐔':
        return '🍗'
    elif ingrediente == '🐮':
        return '🍔'
    elif ingrediente == '🥔':
        return '🍟'
    else:
        return '🍪'
    
# ejecución
ingredientes = ['🐔', '🐮', '🥔']
resultado = map(cocinar, ingredientes)
lista_r = list(resultado)  
print(lista_r)  

# con lambda
ingredientes = ['🐔', '⚽', '🥔']
cocinar_v2 = lambda ingrediente: '🍗' if ingrediente == '🐔' else ('🍔' if ingrediente == '🐮' else ('🍟' if ingrediente == '🥔' else '🍪'))
resultado = map(cocinar_v2, ingredientes)
lista_r = list(resultado)  
print(lista_r)  