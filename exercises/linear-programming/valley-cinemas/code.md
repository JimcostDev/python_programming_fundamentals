# 📝 Explicación del Código - Sistema SilverScreener

## 🎯 Resumen Ejecutivo

Este documento explica el código Python que implementa un modelo de **programación lineal entera** para optimizar la programación de películas en cines multiplex. El sistema resuelve automáticamente qué películas proyectar, cuándo y por cuánto tiempo.

---

## 🏗️ Estructura General del Código

```python
import pulp as pl

def crear_modelo_valley_cinemas():
    # 1. Configuración del problema
    # 2. Definición de datos
    # 3. Generación de programas posibles
    # 4. Creación de variables de decisión
    # 5. Formulación de restricciones
    # 6. Resolución del modelo
    # 7. Procesamiento de resultados
```

---

## 📊 1. Configuración Inicial

### **Propósito**: Crear el problema de optimización base

```python
modelo = pl.LpProblem("Valley_Cinemas_Programacion", pl.LpMinimize)
modelo += 0, "Objetivo_Factibilidad"
```

**¿Qué hace?**
- Crea un problema de **minimización** (aunque minimizamos 0)
- Es un problema de **factibilidad**: buscamos cualquier solución válida, no la "mejor"

**¿Por qué?**
- No tenemos función objetivo específica (como maximizar ganancias)
- Solo queremos una programación que **funcione** y cumpla restricciones

---

## 📋 2. Definición de Datos

### **Propósito**: Establecer parámetros del problema empresarial

```python
peliculas_info = {
    1: (1, 2, 2),  # (primera_semana, ultima_semana, max_duracion)
    2: (1, 3, 2),
    3: (1, 1, 1),
    4: (2, 4, 2),
    5: (3, 4, 3),
    6: (3, 4, 2)
}

NUM_PANTALLAS = 2
SEMANAS = [1, 2, 3, 4]
```

**¿Qué representa cada tupla?**
- **Primera semana**: Cuándo puede empezar la película
- **Última semana**: Cuándo debe terminar máximo
- **Max duración**: Cuántas semanas consecutivas puede durar

**Ejemplo práctico**:
- Película 5: `(3, 4, 3)` → Puede empezar en semana 3 o 4, terminar máximo en semana 4, durar hasta 3 semanas

---

## 🔧 3. Generación de Programas Posibles

### **Propósito**: Crear automáticamente todas las combinaciones válidas

```python
def generar_programas_posibles():
    programas = {}
    
    for pelicula, (primera_sem, ultima_sem, max_dur) in peliculas_info.items():
        programas[pelicula] = []
        
        for inicio in range(primera_sem, ultima_sem + 1):
            for duracion in range(1, max_dur + 1):
                semana_final = inicio + duracion - 1
                
                if semana_final <= ultima_sem:
                    programas[pelicula].append((inicio, duracion))
    
    return programas
```

**Lógica del algoritmo**:
1. **Bucle exterior**: Prueba cada semana de inicio posible
2. **Bucle interior**: Prueba cada duración posible
3. **Validación**: `semana_final <= ultima_sem` asegura que no se pase del límite

**Ejemplo para película 1**:
- `(1, 2, 2)` → Programas posibles:
  - `(1, 1)`: Empieza semana 1, dura 1 semana → termina semana 1 ✅
  - `(1, 2)`: Empieza semana 1, dura 2 semanas → termina semana 2 ✅
  - `(2, 1)`: Empieza semana 2, dura 1 semana → termina semana 2 ✅
  - `(2, 2)`: Empieza semana 2, dura 2 semanas → termina semana 3 ❌ (excede límite)

---

## 🎲 4. Variables de Decisión

### **Propósito**: Definir las incógnitas que el solver debe determinar

```python
x = {}

for pelicula in programas_posibles:
    for idx, (inicio, duracion) in enumerate(programas_posibles[pelicula], 1):
        var_name = f"x_{pelicula}_{idx}"
        x[(pelicula, idx)] = pl.LpVariable(var_name, cat="Binary")
```

**¿Qué son las variables binarias?**
- **x[i,j] = 1**: Seleccionar programa j de película i
- **x[i,j] = 0**: NO seleccionar programa j de película i

**Ejemplo**:
- `x_1_2 = 1` significa: "Seleccionar programa 2 de película 1 (empezar semana 1, durar 2 semanas)"

**¿Por qué usar tuplas como claves?**
- `x[(1,2)]` es más eficiente que buscar en listas
- Acceso directo O(1) en lugar de O(n)

---

## 🔒 5. Restricciones del Modelo

### **A) Restricción de Selección Única**

```python
for pelicula in programas_posibles:
    constraint_vars = [x[(pelicula, idx)] for idx in range(1, len(programas_posibles[pelicula]) + 1)]
    modelo += pl.lpSum(constraint_vars) == 1, f"Unica_seleccion_pelicula_{pelicula}"
```

**Significado matemático**:
- Para película 1: `x_1_1 + x_1_2 + x_1_3 = 1`
- Exactamente **UNA** variable debe ser 1, las demás 0

**¿Por qué es necesaria?**
- Sin ella, el modelo podría seleccionar 0 programas (película no se proyecta)
- O múltiples programas (físicamente imposible)

### **B) Restricción de Capacidad de Pantallas**

```python
def programa_cubre_semana(pelicula, programa_idx, semana_objetivo):
    inicio, duracion = programas_posibles[pelicula][programa_idx - 1]
    return inicio <= semana_objetivo <= inicio + duracion - 1

for semana in SEMANAS:
    variables_semana = []
    
    for pelicula in programas_posibles:
        for programa_idx in range(1, len(programas_posibles[pelicula]) + 1):
            if programa_cubre_semana(pelicula, programa_idx, semana):
                variables_semana.append(x[(pelicula, programa_idx)])
    
    if variables_semana:
        modelo += pl.lpSum(variables_semana) <= NUM_PANTALLAS, f"Capacidad_semana_{semana}"
```

**Función `programa_cubre_semana`**:
- **Input**: película, programa, semana objetivo
- **Output**: ¿Este programa incluye esa semana?
- **Lógica**: `inicio <= semana <= inicio + duracion - 1`

**Ejemplo**:
- Programa que empieza semana 2 y dura 3 semanas cubre semanas 2, 3, 4
- NO cubre semanas 1 o 5

**Restricción final**:
- Para cada semana: suma de programas activos ≤ 2 pantallas
- Para semana 3: `x_2_5 + x_4_3 + x_5_1 + x_6_2 ≤ 2`

---

## 🎯 6. Resolución del Modelo

```python
modelo.solve(pl.PULP_CBC_CMD(msg=0))

estado = pl.LpStatus[modelo.status]

if modelo.status == pl.LpStatusOptimal:
    # Procesar solución
elif modelo.status == pl.LpStatusInfeasible:
    print("❌ PROBLEMA INFACTIBLE")
```

**¿Qué hace `modelo.solve()`?**
- Llama al solver **CBC** (Coin-or Branch and Cut)
- CBC es un solver profesional gratuito para programación entera
- `msg=0` suprime output técnico del solver

**Estados posibles**:
- **LpStatusOptimal**: ✅ Solución encontrada
- **LpStatusInfeasible**: ❌ Imposible satisfacer todas las restricciones
- **LpStatusUnbounded**: ❌ Problema mal formulado

---

## 📊 7. Procesamiento de Resultados

### **A) Identificar Programas Seleccionados**

```python
programas_seleccionados = {}
for pelicula in programas_posibles:
    for programa_idx in range(1, len(programas_posibles[pelicula]) + 1):
        if x[(pelicula, programa_idx)].varValue == 1:
            inicio, duracion = programas_posibles[pelicula][programa_idx - 1]
            programas_seleccionados[pelicula] = (programa_idx, inicio, duracion)
```

**¿Qué hace?**
- Revisa cada variable de decisión
- Si `varValue == 1`, ese programa fue seleccionado
- Guarda información completa: índice, inicio, duración

### **B) Calcular Ocupación por Semana**

```python
for semana in SEMANAS:
    peliculas_semana = []
    for pelicula, (prog_idx, inicio, duracion) in programas_seleccionados.items():
        if inicio <= semana <= inicio + duracion - 1:
            peliculas_semana.append(f"P{pelicula}")
    
    ocupacion = len(peliculas_semana)
    print(f"Semana {semana}: {ocupacion}/{NUM_PANTALLAS} pantallas ocupadas")
```

**Valor empresarial**:
- **Utilización de recursos**: ¿Estamos usando todas las pantallas?
- **Planificación de personal**: ¿Cuántos empleados necesitamos cada semana?
- **Mantenimiento**: ¿Hay semanas con baja ocupación para hacer reparaciones?

---

## 🧮 Complejidad Computacional

### **Variables del modelo**:
```
Total variables = Σ(programas_posibles[i]) para todas las películas i
≈ 24 variables binarias para este caso específico
```

### **Restricciones del modelo**:
```
- Selección única: 6 restricciones (una por película)
- Capacidad: 4 restricciones (una por semana)
Total: 10 restricciones
```

### **Tiempo de ejecución**:
- **Caso pequeño** (6 películas, 4 semanas): < 0.1 segundos
- **Escalabilidad**: O(n×m×s) donde n=películas, m=programas promedio, s=semanas

---

## 🔍 Puntos Clave del Diseño

### **1. Separación de Responsabilidades**
```python
# Datos del negocio
peliculas_info = {...}

# Lógica de generación
def generar_programas_posibles()

# Modelo matemático
modelo = pl.LpProblem(...)

# Procesamiento de resultados
def procesar_solucion()
```

### **2. Validación Robusta**
- Verificar que programas no excedan ventanas permitidas
- Solo crear restricciones cuando hay variables relevantes
- Manejar casos de infactibilidad

### **3. Output Interpretable**
- Traducir variables matemáticas a decisiones de negocio
- Mostrar ocupación por semana para fácil verificación
- Incluir nombres descriptivos para restricciones

---

## 🎯 Aplicaciones Prácticas

Este mismo patrón de código se adapta para:

- **🏥 Hospitales**: Programación de quirófanos y médicos
- **✈️ Aerolíneas**: Asignación de tripulaciones y rutas  
- **🏭 Manufactura**: Planificación de producción y recursos
- **📚 Universidades**: Asignación de aulas y horarios
- **🚛 Logística**: Ruteo de vehículos y distribución

El código es un **template reutilizable** para problemas de asignación con restricciones de capacidad y tiempo.

---

## ⚡ Conclusión

Este código implementa un **sistema profesional de optimización** que:

✅ **Modela problemas empresariales reales** usando matemáticas  
✅ **Genera automáticamente** todas las opciones válidas  
✅ **Resuelve optimalmente** usando solvers industriales  
✅ **Produce resultados interpretables** para toma de decisiones  

Es un ejemplo perfecto de cómo **la programación lineal** convierte problemas complejos del mundo real en soluciones computacionales elegantes y eficientes.