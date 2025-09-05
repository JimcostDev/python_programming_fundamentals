# Exponer el uso básico de la función print
print('Este es un ejemplo básico 1.')

# quitamos el salto de linea, termina en espacio ' '
print('Este es un ejemplo básico 2.', end=' ')
print('Este es un ejemplo básico 3.', end=' ')

print()
# cambiamos el separador
print('Python', 'es', 'genial')
print('Python', 'es', 'genial', sep='-')

# placeholders o cadenas formateadas
print('{} es {}'.format('Python', 'estupendo'))

print()
numeros = [2, 3, 5, 7, 12]
# representacion en cadena de caracteres de esa lista - numeros
print(numeros)

print()
capitales = {'Colombia: ' 'Bogota', 'Argentina: ' 'Buenos Aires'}
# representacion en cadena de caracteres del diccionario - capitales
print(capitales)
