# Un bucle while realiza una operación mientras (while, en inglés) una determinada condición es True
"""
Lo más importante que se debe recordar al crear bucles while es asegurarse de que cambia la condición. 
Si la condición siempre es True, Python seguirá ejecutando el código hasta que el programa se bloquee.

Un bucle while tiene tres partes importantes:

    1. La palabra while, seguida de un espacio.

    2. La condición que se va a probar. Si la condición es True, se ejecutará el código dentro del bucle while.

    3. El código que quiere ejecutar para cada elemento del objeto iterable, seguido de espacios en blanco anidados.

"""

# Agregar elementos (planetas) a una lista y finalizar el proceso escribiendo done
new_planet = ''
planets = []
while new_planet.lower() != 'done':
    if new_planet: # validar que new_planet no este vacio
        print(new_planet)
        planets.append(new_planet)
    new_planet = input('Enter a new planet, or done if done: ')

print(planets)