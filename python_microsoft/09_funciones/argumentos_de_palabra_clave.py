from datetime import timedelta, datetime

def arrival_time(hours=12):
    now = datetime.now()
    arrival = now + timedelta(hours=hours)
    return arrival.strftime("Arrival: %A %H:%M")

print(arrival_time())


"""
Aunque la función define un argumento de palabra clave, no permite pasar uno 
cuando se llama a una función. En este caso, la variable hours tiene como 
valor predeterminado 51. Para comprobar que la fecha actual es correcta,
use 0 como valor para hours:
"""

# Combinación de argumentos y argumentos de palabra clave

def arrival_time_new(destination, hours=12):
    now = datetime.now()
    arrival = now + timedelta(hours=hours)
    return arrival.strftime(f"{destination} Arrival: %A %H:%M")

print(arrival_time_new('Moon'))
