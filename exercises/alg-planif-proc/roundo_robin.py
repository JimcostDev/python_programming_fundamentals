from tabulate import tabulate
from operator import attrgetter

class Proceso(object):
    def __init__(self, id, rafaga, llegada):
        self.id = id
        self.rafaga = rafaga
        self.llegada = llegada
        self.rafaga_tmp = rafaga
        self.espera = 0
        self.retorno = 0
        self.terminacion = 0

def ordenarProcesosPorTiempoLlegada(lista):
    return sorted(lista, key=attrgetter('llegada'))

try:
    procesos = [[0, 10], [1, 4], [2, 8], [3, 5], [4, 12]]
    if len(procesos) > 0:
        lista_procesos = []
        for numero_p, proceso in enumerate(procesos):
            llegada_tmp = proceso[0]
            rafaga_tmp = proceso[1]
            lista_procesos.append(Proceso((numero_p + 1), rafaga_tmp, llegada_tmp))

        quantum = int(input('Ingrese el Quantum: '))

        lista_procesos = ordenarProcesosPorTiempoLlegada(lista_procesos)
        procesos_restantes = len(lista_procesos)
        tiempo = 0
        cola_procesos = []
        proceso_actual = None
        siguiente_proceso = 0

        resultados = []

        while procesos_restantes > 0:
            if len(lista_procesos) > siguiente_proceso and tiempo >= lista_procesos[siguiente_proceso].llegada:
                cola_procesos.append(lista_procesos[siguiente_proceso])
                siguiente_proceso += 1
            else:
                if siguiente_proceso > 0 or len(cola_procesos) > 0:
                    if proceso_actual is None:
                        proceso_actual = cola_procesos.pop(0)
                        control = True

                    if control:
                        if proceso_actual.rafaga_tmp >= quantum:
                            proceso_actual.rafaga_tmp -= quantum
                            tiempo += quantum
                        else:
                            tiempo += proceso_actual.rafaga_tmp
                            proceso_actual.rafaga_tmp = 0

                        if proceso_actual.rafaga_tmp < 1:
                            proceso_actual.terminacion = tiempo
                            proceso_actual.retorno = proceso_actual.terminacion - proceso_actual.llegada
                            proceso_actual.espera = proceso_actual.retorno - proceso_actual.rafaga
                            procesos_restantes -= 1
                            resultados.append([proceso_actual.id, proceso_actual.terminacion, proceso_actual.espera, proceso_actual.retorno])
                            proceso_actual = None
                        else:
                            control = False
                    else:
                        cola_procesos.append(proceso_actual)
                        proceso_actual = None
                else:
                    tiempo += 1

        print()
        print('--------------------------- RESULTADOS --------------------------')
        encabezados = ["Proceso # ", "Terminación", "Tiempo de Espera", "Retorno"]
        tabla = tabulate(resultados, headers=encabezados, tablefmt="grid")
        print(tabla)

        # Cálculo de promedios
        total_retorno = sum(proceso.retorno for proceso in lista_procesos)
        total_espera = sum(proceso.espera for proceso in lista_procesos)
        promedio_retorno = total_retorno / len(lista_procesos)
        promedio_espera = total_espera / len(lista_procesos)

        print(f'Promedio de retorno: {promedio_retorno}')
        print(f'Promedio de espera: {promedio_espera}')
        print()
    else:
        print('El número de procesos debe ser mayor a 0 (cero) para poder probar el algoritmo.')
except Exception as e:
    print(e)
