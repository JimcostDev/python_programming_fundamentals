""""
los diccionarios de Python permiten trabajar con conjuntos de datos relacionados. 
Un diccionario es una colección de pares clave-valor. Piense que es como un grupo 
de variables dentro de un contenedor, donde la clave es el nombre de la variable y 
el valor es el valor almacenado en su interior.
"""
# CREACIÓN
print('**************** CREACIÓN ******************')
planet = {
    'name': 'Earth',
    'moons': 1
}

print(planet.get('name'))
# planet['name'] is identical to using planet.get('name')
print(planet['name'])

# MODIFICACION:
print('**************** MODIFICACION ******************')
planet.update({'name': 'Tierra'})
print(planet.get('name'))

planet['name'] = 'Makemake'
print(planet.get('name'))

# Using update
planet.update({
    'name': 'Jupiter',
    'moons': 79
})

print(planet.get('name'))
print(planet.get('moons'))

# Using square brackets
planet['name'] = 'Olimpo'
planet['moons'] = 12

print(planet.get('name'))
print(planet.get('moons'))

# ADICCIÓN 
print('**************** ADICCIÓN ******************')
planet['orbital period'] = 4333
print(planet)

# ELIMINACIÓN 
print('**************** ELIMINACIÓN ******************')
planet.pop('orbital period')
print(planet)

# ANIDACIÓN
print('**************** ANIDACIÓN ******************')
planet['diameter (km)'] = {
    'polar': 133709,
    'equatorial': 142984
}
print(planet)
print(f'{planet["name"]} polar diameter: {planet["diameter (km)"]["polar"]}')


