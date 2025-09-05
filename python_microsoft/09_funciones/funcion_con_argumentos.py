def distance_from_earth(destination):
    if destination == "Moon":
        return "238,855"
    else:
        return "Unable to compute to that destination"

print(distance_from_earth('Moon'))

# Multiples argumentos

def days_to_complete(distance, speed):
    hours = distance/speed
    return hours/24

print(days_to_complete(238855, 75))


# Funciones como argumentos
total_days = days_to_complete(238855, 75)
round(total_days) # or round(days_to_complete(238855, 75))
print(round(total_days))






