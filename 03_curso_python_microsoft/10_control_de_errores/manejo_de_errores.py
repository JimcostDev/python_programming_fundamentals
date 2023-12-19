countries = {
    'colombia': 50,
    'mexico': 122,
    'argentina': 43,
    'chile': 18,
    'peru': 31
}
while True:
    country = str(input('Escribe el nombre del país del cual quieres saber su población: ')).lower()
    try:
        print('La población de {} es: {} millones'.format(country, countries[country]))
    except KeyError:
        print('No tenemos el dato de la población del país {}'.format(country))
