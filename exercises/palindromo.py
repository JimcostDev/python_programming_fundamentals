def es_palindromo(cadena):
    # Eliminar los espacios y convertir todo a minúsculas
    cadena = cadena.replace(" ", "").lower()
    # Verificar si la cadena es igual a su reverso
    return cadena == cadena[::-1]

# Ejemplo de uso
texto = "Anita lava la tina"
if es_palindromo(texto):
    print(f'"{texto}" es un palíndromo.')
else:
    print(f'"{texto}" no es un palíndromo.')

## texto al reves
# texto = 'hola'
# print(texto[::-1])