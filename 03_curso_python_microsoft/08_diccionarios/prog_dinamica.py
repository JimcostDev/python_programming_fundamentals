rainfall = {
    'october': 3.5,
    'november': 4.2,
    'december': 2.1
}

# Determinación de la existencia de una clave en un diccionario
if 'december' in rainfall:
    rainfall['december'] = rainfall['december'] + 1
else:
    rainfall['december'] = 1

for key in rainfall.keys():
    print(f'{key}: {rainfall[key]}cm')

# Recuperación de todos los valores
"""
De forma similar a keys(), values() devuelve la lista de todos 
los valores de un diccionario sin sus claves
"""

print('************** Values ***********')
total_rainfall = 0
for value in rainfall.values():
    total_rainfall += value # = total_rainfall = total_rainfall + value

print(f'There was {total_rainfall}cm in the last quarter')



