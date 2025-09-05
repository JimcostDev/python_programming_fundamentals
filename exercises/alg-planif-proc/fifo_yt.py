"""
procesos {
    key : value,
    t-llegada : rafaga,
    3, 10
}

nota: el valor de t-llegada (key) debe ser unico
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
            t_llegada = int(input(f'Ingrese el tiempo de llegada ⏱️  del proceso #{pr + 1}: '))
            rafaga= int(input(f'Ingrese el valor de rafaga 🔥 en CPU del proceso #{pr + 1}: '))
            procesos[t_llegada] = rafaga
            print()
            print()
        print('✅✅✅✅✅ ORDENAMOS LOS PROCESOS SEGÚN SU TIEMPO DE LLEGADA ✅✅✅✅✅')
        # ordenar el diccionario a partir de su llave (t-llegada)
        procesos_ordenados = dict(sorted(procesos.items(), key=itemgetter(0)))
        #print(procesos_ordenados) 
        tiempoRespuesta = 0
        totalTR = []
        for t_llegada, rafaga in procesos_ordenados.items():
            tiempoRespuesta += rafaga
            print(f"""
            Proceso con tiempo de llegada: #{t_llegada}
            Tiempo de respuesta: {tiempoRespuesta}
            ------------ Fin del proceso ------------
            """)
            totalTR.append(tiempoRespuesta)

        contador = 0
        tiempoEspera = []
        for te in totalTR:
            contador += 1
            val = te - contador
            tiempoEspera.append(val)

        tiempoEspera = tiempoEspera[:-1]
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
