"""
procesos {
    key : value,
    prioridad : rafaga,
    3, 10
}

nota: el valor de prioridad (key) debe ser unico
"""
from operator import itemgetter
try:
    print('💻💻💻💻💻💻 OBTENEMOS DATOS DE ENTRADA 💻💻💻💻💻💻')
    print()
    cantidad_procesos = int(input('Ingrese el número de procesos: '))
    if(cantidad_procesos > 0):
        procesos = {}
        for pr in range(cantidad_procesos):
            print(f'Proceso #{pr + 1}')
            prioridad = int(input(f'Ingrese el valor de prioridad ⏱️  del proceso #{pr + 1}: '))
            rafaga= int(input(f'Ingrese el valor de rafaga 🔥 en CPU del proceso #{pr + 1}: '))
            procesos[prioridad] = rafaga
            print()
            print()
        print('✅✅✅✅✅ ORDENAMOS LOS PROCESOS SEGÚN SU PRIORIDAD ✅✅✅✅✅')
        # ordenar el diccionario a partir de su llave (prioridad)
        procesos_ordenados = dict(sorted(procesos.items(), key=itemgetter(0)))
        #print(procesos_ordenados) 
        tiempoRespuesta = 0
        totalTR = []
        for prioridad, rafaga in procesos_ordenados.items():
            tiempoRespuesta += rafaga
            print(f"""
            Proceso con prioridad: #{prioridad}
            Tiempo de respuesta: {tiempoRespuesta}
            ------------ Fin del proceso ------------
            """)
            
            totalTR.append(tiempoRespuesta)

        
        tiempoEspera = totalTR[:-1]
        tiempoEspera.append(0)
        tiempoEspera.sort()

        sumatoriaTE = sum(tiempoEspera)
        sumatoriaTR = sum(totalTR)
        
        promedioTE  =  sumatoriaTE / len(procesos_ordenados)
        promedioTR = sumatoriaTR / len(procesos_ordenados)
        print(f'El tiempo de espera {tiempoEspera} promedio es de: {promedioTE} ut.')
        print(f'El tiempo de respuesta {totalTR} promedio es de: {promedioTR} ut.')
    else:
       print('El número de procesos debe ser mayor a 0 (cero) para poder probar el algoritmo.')
except Exception as e:
    print(e)
