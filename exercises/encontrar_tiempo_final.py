"""
    La tarea es preparar un código simple para evaluar o encontrar el tiempo final de un periodo de tiempo dado, 
    expresándolo en horas y minutos. Las horas van de 0 a 23 y los minutes de 0 a 59. 

    Por ejemplo, si el evento comienza a las 12:17 y dura 59 minutos, terminará a las 13:16.
    
    Datos de Prueba
      Entrada de muestra:
      12
      17
      59
      Salida esperada: 13:16


      Entrada de muestra:
      23
      58
      642

      Salida esperada: 10:40
"""

#datos
hora = int(input("Hora de inicio (horas): "))
min = int(input("Minuto de inicio (minutos): "))
dura = int(input("Duración del evento (minutos): "))

#operacion
hora_inicial = "{}:{}".format(hora,min)
print("hora inicial", hora_inicial)

suma = min + dura
 
if suma >= 60:
  dife = suma % 60
  suma_hora = suma // 60
  hora += suma_hora
  if hora > 24:
        hora = 0
        hora += suma_hora - 1
  print(f"Hora final: {hora}:{dife}")
else:
    suma = min + dura
    print(f"Hora final: {hora}:{suma}")