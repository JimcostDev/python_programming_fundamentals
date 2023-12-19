
# funcion que imprime las partes de un cohete
def rocket_parts():
    print("payload, propellant, structure")

# la funcion no devulve ningun valor
output = rocket_parts()
print(output)


"""
Puede parecer sorprendente que el valor de la variable output sea None. 
Esto se debe a que la función rocket_parts() no ha devuelto explícitamente un valor. 
En Python, si una función no devuelve explícitamente un valor, devuelve implícitamente None
"""

"""
 Actualizar la función para devolver la cadena en 
 lugar de imprimirla hace que la variable output tenga un valor distinto:

    >>> def rocket_parts():
        return "payload, propellant, structure"
    >>> output = rocket_parts()
    >>> output
    'payload, propellant, structure'
"""