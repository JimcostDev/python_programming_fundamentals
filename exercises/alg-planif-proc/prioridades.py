"""
procesos {
    key : value,
    prioridad : rafaga,
    3, 10
}

nota: el valor de prioridad (key) debe ser unico
"""
from operator import itemgetter
from tabulate import tabulate

try:
    procesos = [
        {'prioridad': 3, 'rafaga': 10},
        {'prioridad': 1, 'rafaga': 1},
        {'prioridad': 5, 'rafaga': 2},
        {'prioridad': 4, 'rafaga': 1},
        {'prioridad': 2, 'rafaga': 5}
    ]

    cantidad_procesos = len(procesos)

    if cantidad_procesos > 0:
        print('------- ORDENAMOS LOS PROCESOS SEGÚN SU PRIORIDAD --------')
        procesos_ordenados = sorted(procesos, key=itemgetter("prioridad"))
        tiempoRespuesta = 0
        totalTR = []
        tabla_procesos = []

        for proceso in procesos_ordenados:
            prioridad = proceso["prioridad"]
            rafaga = proceso["rafaga"]
            tiempoRespuesta += rafaga
            tabla_procesos.append([prioridad, tiempoRespuesta])

            totalTR.append(tiempoRespuesta)

        # mostrar resultados en tabla
        headers = ["Proceso con prioridad #", "Tiempo de respuesta"]
        tabla_resultados = tabulate(tabla_procesos, headers=headers, tablefmt="grid")
        print(tabla_resultados)
        
        tiempoEspera = totalTR[:-1]
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


