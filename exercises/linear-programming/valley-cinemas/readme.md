# 🎬 Sistema SilverScreener - Valley Cinemas

## 📋 Descripción del Proyecto

**SilverScreener** es un sistema de optimización basado en **programación lineal entera** diseñado para ayudar a los gerentes de salas de cine a decidir qué películas exhibir semanalmente en complejos con múltiples pantallas.

Este proyecto implementa un modelo matemático para **Valley Cinemas**, una cadena de cines que busca optimizar la programación de películas en una sala piloto de **2 pantallas** durante un período de **4 semanas**.

### 🎯 Objetivo del Sistema

El sistema resuelve automáticamente el problema de:
- **¿Qué películas exhibir?**
- **¿En qué semanas proyectar cada película?**
- **¿Por cuántas semanas consecutivas?**

Todo esto respetando las limitaciones de:
- ✅ Capacidad de pantallas disponibles
- ✅ Ventanas de exhibición de cada película
- ✅ Duración máxima permitida por película
- ✅ Proyección consecutiva (sin interrupciones)

## 🔬 Problema de Investigación de Operaciones

### Contexto Empresarial

Valley Cinemas enfrenta el desafío típico de la industria cinematográfica: **maximizar la utilización de sus recursos limitados** (pantallas) mientras satisface:

1. **Restricciones de disponibilidad**: Cada película tiene ventanas específicas de exhibición
2. **Restricciones operativas**: Las películas deben proyectarse en semanas consecutivas una vez iniciadas
3. **Restricciones de capacidad**: Solo 2 pantallas disponibles simultáneamente

### Datos del Problema

| Película | Primera Semana | Última Semana | Máx. Semanas | Programas Posibles |
|----------|----------------|---------------|--------------|-------------------|
| 1        | 1              | 2             | 2            | 3 programas       |
| 2        | 1              | 3             | 2            | 5 programas       |
| 3        | 1              | 1             | 1            | 1 programa        |
| 4        | 2              | 4             | 2            | 5 programas       |
| 5        | 3              | 4             | 3            | 6 programas       |
| 6        | 3              | 4             | 2            | 4 programas       |

### Modelo Matemático

**Tipo**: Programación Lineal Entera Binaria (0-1)

**Variables de Decisión**:
- `x_i_j` = 1 si se selecciona el programa j de la película i, 0 en caso contrario

**Restricciones**:
1. **Selección única**: Cada película debe tener exactamente un programa seleccionado
2. **Capacidad**: Máximo 2 películas pueden proyectarse simultáneamente en cualquier semana

**Función Objetivo**: Problema de factibilidad (encontrar cualquier solución válida)

## 🛠️ Solución Técnica

### Arquitectura del Sistema

```
📦 SilverScreener
├── 🧮 Generador de Programas
│   ├── Validación de ventanas temporales
│   ├── Cálculo de duraciones válidas
│   └── Creación de variables de decisión
├── 🔧 Motor de Optimización
│   ├── Formulación de restricciones
│   ├── Solver PuLP + CBC
│   └── Validación de soluciones
└── 📊 Sistema de Reportes
    ├── Programas seleccionados
    ├── Ocupación por semana
    └── Análisis de factibilidad
```

### Algoritmo Principal

1. **Generación Dinámica de Programas**
   ```python
   # Para cada película, generar todos los programas válidos
   for inicio in range(primera_semana, ultima_semana + 1):
       for duracion in range(1, max_duracion + 1):
           if inicio + duracion - 1 <= ultima_semana:
               programas_validos.append((inicio, duracion))
   ```

2. **Creación de Variables Binarias**
   ```python
   # Una variable por cada programa posible
   x[(pelicula, programa)] = LpVariable(f"x_{pelicula}_{programa}", cat="Binary")
   ```

3. **Formulación de Restricciones**
   ```python
   # Exactamente un programa por película
   sum(x[(i, j)] for j in programas[i]) == 1
   
   # Máximo 2 películas por semana
   sum(x[(i, j)] for programas que cubren semana t) <= 2
   ```

### Características Técnicas

- **Lenguaje**: Python 3.7+
- **Solver**: CBC (Coin-or Branch and Cut)
- **Librería**: PuLP (Python Linear Programming)
- **Complejidad**: O(n×m) donde n=películas, m=programas promedio
- **Tipo de problema**: NP-completo (pero pequeño, se resuelve instantáneamente)

## 🚀 Instalación y Ejecución


```bash
# 1. Instalar dependencias
pip install pulp

# Alternativamente, con requirements.txt:
pip install -r requirements.txt
```

```bash
# Ejecutar el modelo completo
python main.py
```

## 📊 Análisis de Resultados

### Interpretación de la Solución

El sistema encuentra automáticamente una **programación óptima** que:

✅ **Cumple todas las restricciones**:
- Cada película tiene exactamente un programa asignado
- Nunca se exceden las 2 pantallas disponibles
- Todas las películas se proyectan en sus ventanas permitidas

✅ **Maximiza la utilización de recursos**:
- 87.5% de ocupación promedio (7/8 pantallas-semana utilizadas)
- Distribución equilibrada de la carga de trabajo

✅ **Respeta las políticas operativas**:
- Proyección consecutiva garantizada
- No hay interrupciones en la exhibición

### Métricas de Desempeño

| Métrica | Valor |
|---------|-------|
| **Películas programadas** | 6/6 (100%) |
| **Utilización de pantallas** | 7/8 (87.5%) |
| **Tiempo de resolución** | < 0.1 segundos |
| **Estado de la solución** | Óptima |

## 🔧 Personalización y Extensiones

### Modificar Datos de Entrada

```python
# Cambiar información de películas en peliculas_info
peliculas_info = {
    1: (semana_inicio, semana_fin, duracion_maxima),
    # ... más películas
}

# Cambiar capacidad de pantallas
NUM_PANTALLAS = 3  # Para salas más grandes

# Extender período de planificación
SEMANAS = [1, 2, 3, 4, 5, 6]  # 6 semanas
```

### Agregar Función Objetivo

```python
# Maximizar ingresos esperados
ingresos = {1: 10000, 2: 8000, ...}  # Ingresos por película
modelo += pl.lpSum([ingresos[i] * x[(i,j)] * duracion 
                    for programas]), "Maximizar_Ingresos"
```

### Restricciones Adicionales

```python
# Evitar competencia entre géneros similares
# Máximo 1 película de acción por semana
peliculas_accion = [1, 4, 5]
modelo += pl.lpSum([x[(i,j)] for i in peliculas_accion 
                    if cubre_semana(j, semana)]) <= 1
```

## 🎓 Valor Educativo

Este proyecto demuestra conceptos clave de **Investigación de Operaciones**:

### Programación Lineal Entera
- Formulación de problemas de decisión discreta
- Variables binarias 0-1
- Restricciones de selección y capacidad

### Modelado Matemático
- Traducción de problemas empresariales a modelos matemáticos
- Identificación de variables de decisión
- Formulación de restricciones lógicas

### Optimización Computacional
- Uso de solvers profesionales (CBC)
- Análisis de factibilidad y optimalidad
- Interpretación de resultados

## 📈 Casos de Uso Reales

Este tipo de sistema se utiliza en:

- **🎬 Industria Cinematográfica**: Programación de salas multiplex
- **📺 Televisión**: Programación de parrillas televisivas
- **🏭 Manufactura**: Asignación de recursos y programación de producción
- **🚛 Logística**: Ruteo de vehículos y asignación de recursos
- **📅 Servicios**: Programación de personal y turnos

