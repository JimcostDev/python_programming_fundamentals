# Simulación de algoritmo de planificación de procesos Round Robin (turno rotatorio)
class process(object):
    def __init__(self, id, burst, arrival):
        self.id = id
        self.burst = burst  # rafaga
        self.arrival = arrival  # llegada
        self.burst_tmp = burst
        self.wait = 0
        self.return_ = 0
        self.ending = 0


try:
    number_processes = int(input('Ingrese el número de procesos: '))
    if (number_processes > 0):
        process_list = []
        for number_p in range(number_processes):
            arrival_tmp = -1
            print(f'💻💻💻💻💻 Proceso #{number_p + 1} 💻💻💻💻💻')
            while (arrival_tmp < 0):
                arrival_tmp = int(
                    input(f'Ingrese el ⏱️  tiempo de llegada del proceso #{number_p + 1}: '))

            burst_tmp = 0
            while (burst_tmp < 1):
                burst_tmp = int(
                    input(f'Ingrese la 🔥 rafaga del proceso #{number_p + 1}: '))
            #id, burst, arrival
            process_list.append(
                process((number_p + 1), burst_tmp, arrival_tmp))
            print(f'💻💻💻💻💻 Fin del proceso 💻💻💻💻💻')
            print()
            print()
            print()
        quantum = 0
        while (quantum < 1):
            quantum = int(input('Ingrese el Quantum: '))
        quantum_tmp = quantum

        # FUNCIÓN PARA CALCULAR EL ORDEN DE LOS PROCESOS SEGUN EL TIEMPO DE LLEGADA
        def orderProcessForTimeArrival(list):
            for proc in range(1, len(list)):
                item = proc
                while (item > 0 and list[item].arrival < list[item-1].arrival):
                    list[item], list[item-1] = list[item-1], list[item]
                    item = item-1
            return list
        process_list = orderProcessForTimeArrival(
            process_list)  # se ordena por tiempo de llegada
        # controla los procesos que hacen falta por terminar
        mirror_process = len(process_list)
        time = 0
        tail_processes = []
        currently_execution_proccess = None  # proceso actualmente en ejecución
        next_process = 0
        print(
            '💡 Se activa el algoritmo Round Robin (turno rotatorio) 😁')
        print()
        print()
        control = True
        while (mirror_process > 0):
            print(
                f' *************************** Tiempo: {time} ************************')
            if (len(process_list) > next_process and time >= process_list[next_process].arrival):
                print(
                    f'💡 El proceso {process_list[next_process].id} se ingreso a la cola de listos')
                tail_processes.append(process_list[next_process])
                next_process += 1
            else:
                if next_process > 0 or len(tail_processes) > 0:
                    if (currently_execution_proccess == None):
                        currently_execution_proccess = tail_processes.pop(
                            0)
                        control = True
                        print(
                            f'💡 Se saca el proceso {currently_execution_proccess.id} de la cola y se ejecuta.')

                    if (control):
                        if (currently_execution_proccess.burst_tmp >= quantum):
                            currently_execution_proccess.burst_tmp = currently_execution_proccess.burst_tmp - quantum
                            print(
                                f'💡 Se resta {quantum} a la rafaga del proceso {currently_execution_proccess.id}')
                            time = time + quantum
                            print(f'💡 Se aumenta {quantum} al tiempo')
                        else:
                            time = time + currently_execution_proccess.burst_tmp
                            print(
                                f'💡 Se aumenta {currently_execution_proccess.burst_tmp} al tiempo')
                            print(
                                f'💡 Se resta {currently_execution_proccess.burst_tmp}  a la rafaga del proceso {currently_execution_proccess.id}')
                            currently_execution_proccess.burst_tmp = 0

                        if (currently_execution_proccess.burst_tmp < 1):
                            print(
                                f' *************************** Tiempo: {time} ************************')
                            print(
                                f'💡 El Proceso {currently_execution_proccess.id} finalizo.')
                            currently_execution_proccess.ending = time
                            currently_execution_proccess.return_ = currently_execution_proccess.ending - \
                                currently_execution_proccess.arrival
                            currently_execution_proccess.wait = currently_execution_proccess.return_ - \
                                currently_execution_proccess.burst
                            mirror_process = mirror_process - 1
                            currently_execution_proccess = None

                        else:
                            control = False
                    else:
                        tail_processes.append(currently_execution_proccess)
                        print(
                            f'💡 Se agrega el proceso {currently_execution_proccess.id} que estaba en ejecusion a la cola de listos')
                        currently_execution_proccess = None
                else:
                    time += 1
        print('💻💻💻💻💻 Algoritmo finalizado 💻💻💻💻💻')
        print()
        print()
        print()
        print('✅✅✅✅✅ RESULTADOS ✅✅✅✅✅')
        total_return = 0
        total_wait = 0
        for process in process_list:
            print(
                f'Proceso #{process.id}, finalizo: {process.ending}, tiempo de espera: {process.wait}, retorno: {process.return_}')
            total_return = total_return + process.return_
            total_wait = total_wait + process.wait
            print(f'Promedio de retorno: {total_return/len(process_list)}')
            print(f'Promedio de espera: {total_wait/len(process_list)}')
            print()
    else:
        print('El número de procesos debe ser mayor a 0 (cero) para poder probar el algoritmo.')
except Exception as e:
    print(e)
