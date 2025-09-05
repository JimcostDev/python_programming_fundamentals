from datetime import date

# program.py
sum = 1 + 2 # 3
product = sum * 2
print(product)


# tipos de datos
planets_in_solar_system = 8 # int, pluto used to be the 9th planet, but is too small
distance_to_alpha_centauri = 4.367 # float, lightyears
can_liftoff = True
shuttle_landed_on_the_moon = "Apollo 11" #string

tipo = type(planets_in_solar_system)

print(f'la variable {planets_in_solar_system} es de tipo: {tipo}' )

hoy = date.today()

print(f'la fecha de hoy es {hoy}')


