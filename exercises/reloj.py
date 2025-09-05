import time
import datetime

# simulación de un reloj
H = 0 # Horas
M = 0 # Minutos
S = 0 # Segundos

while True:
    # aumentar segundos 
    S += 1
    time.sleep(1)
    if (S == 60):
        S = 0
        M += 1
    # aumentar minutos     
    if (M == 60):
        S = 0
        M = 0
        H += 1
    # aumentar horas 
    if (H == 24):
        S = 0
        M = 0
        H = 0
    if (H == 23 and M == 59 and S == 59):
        break
    # formatear la hora
    hora_formateada = datetime.datetime(1, 1, 1, H, M, S).strftime("%H:%M:%S")
    print(hora_formateada, end="", flush=True)  
    print("\r", end="", flush=True)


