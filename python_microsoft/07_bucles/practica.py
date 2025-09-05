new_planet = ''
planets = []

while new_planet.lower() != 'ok':
    if new_planet:
        planets.append(new_planet)
    new_planet = input('Enter a new planet or done if done: ')

for planet in planets:
    print(planet)