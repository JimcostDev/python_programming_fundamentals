
"""
args permite pasar un número variable de argumentos posicionales a una función. 
Estos argumentos se empaquetan en una tupla dentro de la función.
"""
def suma(*args):
    resultado = 0
    for numero in args:
        resultado += numero
    return resultado

print(suma(1, 2, 3, 4))  # Imprime 10

"""
kwargs permite pasar un número variable de argumentos con nombre (keyword arguments) a una función. 
Estos argumentos se empaquetan en un diccionario dentro de la función.
"""

def informacion_persona(**kwargs):
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")

informacion_persona(nombre="Jhon Doe", edad=30, ciudad="Cali")