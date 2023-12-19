planet_moons = {
    'mercury': 0,
    'venus': 0,
    'earth': 1,
    'mars': 2,
    'jupiter': 79,
    'saturn': 82,
    'uranus': 27,
    'neptune': 14,
    'pluto': 5,
    'haumea': 2,
    'makemake': 1,
    'eris': 1
}

moons = planet_moons.values()
print(moons)
total_planets = len(planet_moons.keys())
print(total_planets)

# calcular el total de lunas
total_moons = 0
for moon in moons:
    total_moons += moon
print(total_moons)

# calcular el promedio de lunas
average = total_moons / total_planets

print(f'Each planet as an average of {average} moons')