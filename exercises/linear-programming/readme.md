# 🏋️‍♂️ Better Fitness Inc. - Optimización de Producción

## 📋 Descripción del Proyecto

Este proyecto resuelve un problema de optimización de producción para **Better Fitness, Inc. (BFI)**, empresa fabricante de equipos de ejercicio que debe determinar la estrategia óptima de producción para dos nuevas máquinas de pesas: **BodyPlus 100** y **BodyPlus 200**.

## 🎯 Objetivo

Determinar la cantidad óptima de cada máquina a producir para **maximizar las utilidades** considerando las limitaciones de recursos disponibles y restricciones del mercado.

## 🏭 Problema de Negocio

### Productos
- **BodyPlus 100**: Máquina básica (estructura + estación prensa + pec-dec)
- **BodyPlus 200**: Máquina avanzada (estructura + estación prensa + pec-dec + prensa piernas)

### Precios de Venta
- **BodyPlus 100**: $1,680 (70% de $2,400 precio retail)
- **BodyPlus 200**: $2,450 (70% de $3,500 precio retail)

### Recursos Limitados
- ⚙️ **Mecanizado y Sujeción**: 600 horas ($20/hora)
- 🎨 **Pintura y Acabado**: 450 horas ($15/hora)  
- 📦 **Ensamblaje y Empaque**: 140 horas ($12/hora)

### Restricciones Especiales
- BodyPlus 200 debe representar **mínimo 25%** de la producción total

## 🧮 Modelo Matemático

### Variables de Decisión
- `x1` = Unidades de BodyPlus 100 a producir
- `x2` = Unidades de BodyPlus 200 a producir

### Función Objetivo
```
Maximizar Z = 371*x1 + 361*x2
```

### Restricciones
```
8*x1  + 12*x2 ≤ 600  (Mecanizado)
5*x1  + 10*x2 ≤ 450  (Pintura)  
2*x1  + 2*x2  ≤ 140  (Ensamblaje)
x1 - 3*x2     ≤ 0    (Mezcla: x2 ≥ 25%)
x1, x2        ≥ 0    (No negatividad)
```

## 💰 Cálculo de Utilidades

### BodyPlus 100
| Concepto | Valor |
|----------|-------|
| Precio de venta | $1,680 |
| Costos materiales | $1,050 |
| Costos mano de obra | $259 |
| **Utilidad unitaria** | **$371** |

### BodyPlus 200  
| Concepto | Valor |
|----------|-------|
| Precio de venta | $2,450 |
| Costos materiales | $1,675 |
| Costos mano de obra | $414 |
| **Utilidad unitaria** | **$361** |


## 📊 Resultados Esperados

El programa mostrará:

- ✅ **Solución óptima**: Cantidades a producir de cada máquina
- 💵 **Utilidad máxima** alcanzable
- 📈 **Uso de recursos** con análisis de holguras
- 🔍 **Restricciones activas** e inactivas
- 📋 **Recomendaciones gerenciales**


## 📈 Análisis de Sensibilidad

El código incluye análisis para identificar:
- **Recursos cuello de botella** (restricciones activas)
- **Recursos subutilizados** (con holgura)
- **Impacto de la restricción del 25%**

## 🎓 Aplicación Académica

Este proyecto forma parte del curso de **Investigación de Operaciones** y abarca:

- ✏️ **Modelado de problemas** de programación lineal
- 📊 **Método gráfico** de solución (para validación)
- 💻 **Software especializado** (GLPK/PuLP)
- 🔬 **Análisis de sensibilidad**


## 🚀 Instalación y Uso

1. Clona el repositorio.
2. Instala las dependencias con:
   ```bash
   pip install pulp
   ```
3. Ejecuta el script principal:
 ```bash
   python main.py
 ```


⭐ **¿Te gustó el proyecto? ¡Dale una estrella en GitHub!**