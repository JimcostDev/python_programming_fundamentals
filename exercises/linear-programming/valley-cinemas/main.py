import pulp as pl

# =============================================================================
# MODELO DE PROGRAMACIÓN LINEAL PARA VALLEY CINEMAS
# Sistema SilverScreener - Programación de películas en sala de 2 pantallas
# =============================================================================

def crear_modelo_valley_cinemas():
    """
    Crea y resuelve el modelo de programación de películas para Valley Cinemas
    """
    
    # Crear el problema de optimización
    # Como no se especifica función objetivo, usamos factibilidad (minimizar 0)
    modelo = pl.LpProblem("Valley_Cinemas_Programacion", pl.LpMinimize)
    
    # Función objetivo: Solo buscamos factibilidad (cualquier solución válida)
    modelo += 0, "Objetivo_Factibilidad"
    
    # =============================================================================
    # DATOS DEL PROBLEMA
    # =============================================================================
    
    # Información de películas: (primera_semana, ultima_semana, max_semanas)
    peliculas_info = {
        1: (1, 2, 2),  # Película 1: disponible semanas 1-2, máximo 2 semanas
        2: (1, 3, 2),  # Película 2: disponible semanas 1-3, máximo 2 semanas  
        3: (1, 1, 1),  # Película 3: disponible semana 1, máximo 1 semana
        4: (2, 4, 2),  # Película 4: disponible semanas 2-4, máximo 2 semanas
        5: (3, 4, 3),  # Película 5: disponible semanas 3-4, máximo 3 semanas
        6: (3, 4, 2)   # Película 6: disponible semanas 3-4, máximo 2 semanas
    }
    
    # Número de pantallas disponibles y semanas del período
    NUM_PANTALLAS = 2
    SEMANAS = [1, 2, 3, 4]
    
    # =============================================================================
    # GENERACIÓN DE PROGRAMAS POSIBLES
    # =============================================================================
    
    def generar_programas_posibles():
        """
        Genera todos los programas posibles para cada película
        Programa = (semana_inicio, duracion)
        """
        programas = {}
        
        for pelicula, (primera_sem, ultima_sem, max_dur) in peliculas_info.items():
            programas[pelicula] = []
            
            # Para cada posible semana de inicio
            for inicio in range(primera_sem, ultima_sem + 1):
                # Para cada posible duración
                for duracion in range(1, max_dur + 1):
                    semana_final = inicio + duracion - 1
                    
                    # Verificar que el programa no exceda la última semana permitida
                    if semana_final <= ultima_sem:
                        programas[pelicula].append((inicio, duracion))
            
            print(f"Película {pelicula}: {len(programas[pelicula])} programas posibles")
            for i, (inicio, dur) in enumerate(programas[pelicula], 1):
                print(f"  Programa {i}: Semana {inicio}, Duración {dur} semanas")
        
        return programas
    
    programas_posibles = generar_programas_posibles()
    
    # =============================================================================
    # VARIABLES DE DECISIÓN
    # =============================================================================
    
    # Variables binarias X_ij donde:
    # i = película, j = índice del programa
    x = {}
    
    print("\n" + "="*50)
    print("VARIABLES DE DECISIÓN CREADAS:")
    print("="*50)
    
    for pelicula in programas_posibles:
        for idx, (inicio, duracion) in enumerate(programas_posibles[pelicula], 1):
            var_name = f"x_{pelicula}_{idx}"
            x[(pelicula, idx)] = pl.LpVariable(var_name, cat="Binary")
            print(f"{var_name}: Película {pelicula}, Programa {idx} "
                  f"(Inicia semana {inicio}, Duración {duracion})")
    
    # =============================================================================
    # RESTRICCIONES
    # =============================================================================
    
    print("\n" + "="*50)
    print("RESTRICCIONES DEL MODELO:")
    print("="*50)
    
    # 1. RESTRICCIONES DE SELECCIÓN ÚNICA POR PELÍCULA
    print("\n1. SELECCIÓN ÚNICA POR PELÍCULA:")
    for pelicula in programas_posibles:
        constraint_vars = [x[(pelicula, idx)] for idx in range(1, len(programas_posibles[pelicula]) + 1)]
        modelo += pl.lpSum(constraint_vars) == 1, f"Unica_seleccion_pelicula_{pelicula}"
        print(f"   Película {pelicula}: Exactamente 1 programa debe ser seleccionado")
    
    # 2. RESTRICCIONES DE CAPACIDAD POR SEMANA
    print("\n2. CAPACIDAD DE PANTALLAS POR SEMANA:")
    
    def programa_cubre_semana(pelicula, programa_idx, semana_objetivo):
        """
        Determina si un programa específico de una película cubre una semana dada
        """
        inicio, duracion = programas_posibles[pelicula][programa_idx - 1]
        return inicio <= semana_objetivo <= inicio + duracion - 1
    
    for semana in SEMANAS:
        variables_semana = []
        peliculas_en_semana = []
        
        for pelicula in programas_posibles:
            for programa_idx in range(1, len(programas_posibles[pelicula]) + 1):
                if programa_cubre_semana(pelicula, programa_idx, semana):
                    variables_semana.append(x[(pelicula, programa_idx)])
                    inicio, duracion = programas_posibles[pelicula][programa_idx - 1]
                    peliculas_en_semana.append(f"P{pelicula}_Prog{programa_idx}")
        
        if variables_semana:  # Solo agregar restricción si hay variables
            modelo += pl.lpSum(variables_semana) <= NUM_PANTALLAS, f"Capacidad_semana_{semana}"
            print(f"   Semana {semana}: Máximo {NUM_PANTALLAS} películas simultáneas")
            print(f"     Variables que cubren esta semana: {', '.join(peliculas_en_semana)}")
    
    # =============================================================================
    # RESOLVER EL MODELO
    # =============================================================================
    
    print("\n" + "="*50)
    print("RESOLVIENDO EL MODELO...")
    print("="*50)
    
    # Resolver el problema
    modelo.solve(pl.PULP_CBC_CMD(msg=0))  # msg=0 para suprimir output del solver
    
    # Verificar el estado de la solución
    estado = pl.LpStatus[modelo.status]
    print(f"Estado de la solución: {estado}")
    
    if modelo.status == pl.LpStatusOptimal:
        print("\n" + "="*50)
        print("SOLUCIÓN ÓPTIMA ENCONTRADA:")
        print("="*50)
        
        # Mostrar programas seleccionados
        programas_seleccionados = {}
        for pelicula in programas_posibles:
            for programa_idx in range(1, len(programas_posibles[pelicula]) + 1):
                if x[(pelicula, programa_idx)].varValue == 1:
                    inicio, duracion = programas_posibles[pelicula][programa_idx - 1]
                    programas_seleccionados[pelicula] = (programa_idx, inicio, duracion)
                    print(f"Película {pelicula}: Programa {programa_idx} "
                          f"(Inicia semana {inicio}, Duración {duracion} semanas)")
        
        # Mostrar ocupación por semana
        print("\n" + "="*30)
        print("OCUPACIÓN POR SEMANA:")
        print("="*30)
        
        for semana in SEMANAS:
            peliculas_semana = []
            for pelicula, (prog_idx, inicio, duracion) in programas_seleccionados.items():
                if inicio <= semana <= inicio + duracion - 1:
                    peliculas_semana.append(f"P{pelicula}")
            
            ocupacion = len(peliculas_semana)
            print(f"Semana {semana}: {ocupacion}/{NUM_PANTALLAS} pantallas ocupadas "
                  f"-> Películas: {', '.join(peliculas_semana) if peliculas_semana else 'Ninguna'}")
    
    elif modelo.status == pl.LpStatusInfeasible:
        print("❌ PROBLEMA INFACTIBLE: No existe solución que satisfaga todas las restricciones")
    else:
        print(f"❌ PROBLEMA NO RESUELTO: {estado}")
    
    return modelo, programas_posibles, x

# =============================================================================
# FUNCIÓN PARA RESPONDER LAS PREGUNTAS ESPECÍFICAS
# =============================================================================

def responder_preguntas():
    """
    Responde las preguntas específicas del problema
    """
    print("\n" + "="*60)
    print("RESPUESTAS A LAS PREGUNTAS DEL PROBLEMA:")
    print("="*60)
    
    # Generar programas para análisis
    peliculas_info = {
        1: (1, 2, 2), 2: (1, 3, 2), 3: (1, 1, 1), 
        4: (2, 4, 2), 5: (3, 4, 3), 6: (3, 4, 2)
    }
    
    def generar_programas(pelicula):
        primera_sem, ultima_sem, max_dur = peliculas_info[pelicula]
        programas = []
        for inicio in range(primera_sem, ultima_sem + 1):
            for duracion in range(1, max_dur + 1):
                if inicio + duracion - 1 <= ultima_sem:
                    programas.append((inicio, duracion))
        return programas
    
    # a) Programas de película 1
    programas_p1 = generar_programas(1)
    print(f"a) Película 1 tiene {len(programas_p1)} programas:")
    for i, (inicio, dur) in enumerate(programas_p1, 1):
        print(f"   x_1_{i}: Inicia semana {inicio}, duración {dur}")
    
    # b) Restricción película 1
    print(f"\nb) Restricción para película 1:")
    vars_p1 = [f"x_1_{i}" for i in range(1, len(programas_p1) + 1)]
    print(f"   {' + '.join(vars_p1)} = 1")
    
    # c) Restricción película 5
    programas_p5 = generar_programas(5)
    print(f"\nc) Restricción para película 5:")
    vars_p5 = [f"x_5_{i}" for i in range(1, len(programas_p5) + 1)]
    print(f"   {' + '.join(vars_p5)} = 1")
    
    # d) Restricción semana 1
    print(f"\nd) Restricción para semana 1:")
    print("   Las 2 pantallas disponibles limitan a máximo 2 películas simultáneas")
    print("   Variables que cubren semana 1: todas que inicien en semana 1")
    
    # e) Restricción semana 3  
    print(f"\ne) Restricción para semana 3:")
    print("   Máximo 2 películas pueden proyectarse simultáneamente")
    print("   Variables que cubren semana 3: programas que incluyan la semana 3")

# =============================================================================
# EJECUCIÓN PRINCIPAL
# =============================================================================

if __name__ == "__main__":
    print("SISTEMA SILVERSCREENER - VALLEY CINEMAS")
    print("Modelo de Programación Lineal Entera para Cines")
    print("="*60)
    
    # Responder preguntas teóricas
    responder_preguntas()
    
    # Crear y resolver el modelo
    modelo, programas, variables = crear_modelo_valley_cinemas()
    
    print("\n" + "="*60)
    print("MODELO COMPLETADO")
    print("="*60)