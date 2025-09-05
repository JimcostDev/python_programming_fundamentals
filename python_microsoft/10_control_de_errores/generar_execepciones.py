
"""
los astronautas limitan su uso de agua a unos 11 litros al día. 
Vamos a crear una función que, en base al número de astronautas, 
pueda calcular la cantidad de agua quedará después de un día o más:
"""

def water_left(astronauts, water_left, days_left):
    daily_usage = astronauts * 11
    total_usage = daily_usage * days_left
    total_water_left = water_left - total_usage
    if total_water_left < 0:
        raise RuntimeError(f"There is not enough water for {astronauts} astronauts after {days_left} days!")
    return f"Total water left after {days_left} days is: {total_water_left} liters"

try:
    water_left(5, 100, 2)
except RuntimeError as err:
    print(err)