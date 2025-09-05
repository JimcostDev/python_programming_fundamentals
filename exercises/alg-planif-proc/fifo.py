"""
procesos {
    key : value,
    t-llegada : rafaga,
    3, 10
}

nota: el valor de t-llegada (key) debe ser unico
"""
from operator import itemgetter
from tabulate import tabulate

try:
    procesos = [
        {'t-llegada': 0, 'rafaga': 10},
        {'t-llegada': 2, 'rafaga': 12},
        {'t-llegada': 4, 'rafaga': 5},
        {'t-llegada': 3, 'rafaga': 6},
        {'t-llegada': 1, 'rafaga': 24}
    ]
    
    cantidad_procesos = len(procesos)
    
    if cantidad_procesos > 0:
        print('--------- ORDENAMOS LOS PROCESOS SEGÚN SU TIEMPO DE LLEGADA ---------')
        
        procesos_ordenados = sorted(procesos, key=itemgetter('t-llegada'))
        
        tiempoRespuesta = 0
        totalTR = []
        tabla_procesos = []

        for proceso in procesos_ordenados:
            t_llegada = proceso['t-llegada']
            rafaga = proceso['rafaga']
            tiempoRespuesta += rafaga
            tabla_procesos.append([t_llegada, tiempoRespuesta])
            
            totalTR.append(tiempoRespuesta)
        
        # mostrar resultados en tabla
        headers = ["Proceso con tiempo de llegada #", "Tiempo de respuesta"]
        tabla_resultados = tabulate(tabla_procesos, headers=headers, tablefmt="grid")
        print(tabla_resultados)

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
        
        promedioTE = sumatoriaTE / len(procesos_ordenados)
        promedioTR = sumatoriaTR / len(procesos_ordenados)
        
        print(f'El tiempo de espera {tiempoEspera} promedio es de: {promedioTE} ut.')
        print(f'El tiempo de respuesta {totalTR} promedio es de: {promedioTR} ut.')
    else:
        print('El número de procesos debe ser mayor a 0 (cero) para poder probar el algoritmo.')
except Exception as e:
    print(e)
