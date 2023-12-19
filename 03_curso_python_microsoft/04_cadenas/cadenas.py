# Metodos
print('###  Metodos ')
cadena = 'temperatures and facts about the moon'
print(cadena.title())
print(cadena.find('moon'))
print(cadena.lower())
print(cadena.upper())

s = "Saturn has a daytime temperature of -170 degrees Celsius, while Mars has -28 Celsius.".replace("Celsius", "C")
print (s)

print()

# División de una cadena
print('### División de una cadena')
temperatures = """Daylight: 260 F
Nighttime: -280 F"""
print(temperatures.split())
print(temperatures.split('\n'))
print(type(temperatures.split())) # list or array
print()

# Búsqueda de una cadena
print('### Búsqueda de una cadena')
luna_ = "Moon" in "This text will describe facts and challenges with space travel"
print(luna_)
luna = "Moon" in "This text will describe facts about the Moon"
print(luna)

# Ejemplo
mars_temperature = "The highest temperature on Mars is about 30 C"
for item in mars_temperature.split():
    if item.isnumeric():
        print(item)

print()

