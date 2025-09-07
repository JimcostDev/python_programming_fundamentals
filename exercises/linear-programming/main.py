# Importamos la biblioteca PuLP
from pulp import *

# Creamos el problema de maximización
prob = LpProblem("BodyPlus_Optimization", LpMaximize)

# ===============================
# CÁLCULO DE UTILIDADES 
# ===============================

# BodyPlus 100:
# Precio venta: $2,400 * 0.70 = $1,680
# Costos materiales: $450 + $300 + $250 + $50 = $1,050
# Horas totales: 8h mecanizado + 5h pintura + 2h ensamblaje = 15h
# Costos mano obra: 8*$20 + 5*$15 + 2*$12 = $160 + $75 + $24 = $259
# Utilidad = $1,680 - $1,050 - $259 = $371  

# BodyPlus 200:
# Precio venta: $3,500 * 0.70 = $2,450
# Costos materiales: $650 + $400 + $250 + $300 + $75 = $1,675
# Horas totales: 12h mecanizado + 10h pintura + 2h ensamblaje = 24h
# Costos mano obra: 12*$20 + 10*$15 + 2*$12 = $240 + $150 + $24 = $414
# Utilidad = $2,450 - $1,675 - $414 = $361  

profit1 = 371  # Utilidad BodyPlus 100
profit2 = 361  # Utilidad BodyPlus 200

print("=== CÁLCULO DE UTILIDADES ===")
print(f"BodyPlus 100: Precio ${1680} - Materiales ${1050} - M.Obra ${259} = ${profit1}")
print(f"BodyPlus 200: Precio ${2450} - Materiales ${1675} - M.Obra ${414} = ${profit2}")

# Definimos las variables de decisión
x1 = LpVariable("x1", lowBound=0, cat='Continuous')  # BodyPlus 100
x2 = LpVariable("x2", lowBound=0, cat='Continuous')  # BodyPlus 200

# Añadimos la función objetivo
prob += profit1 * x1 + profit2 * x2, "Total_Profit"

# ===============================
# RESTRICCIONES
# ===============================

# TIEMPO DE MECANIZADO (por unidad):
# BodyPlus 100: 4 + 2 + 2 = 8 horas 
# BodyPlus 200: 5 + 3 + 2 + 2 = 12 horas 
prob += 8 * x1 + 12 * x2 <= 600, "Mecanizado"

# TIEMPO DE PINTURA (por unidad):
# BodyPlus 100: 2 + 1 + 2 = 5 horas 
# BodyPlus 200: 4 + 2 + 2 + 2 = 10 horas 
prob += 5 * x1 + 10 * x2 <= 450, "Pintura"

# TIEMPO DE ENSAMBLAJE (por unidad):
# BodyPlus 100: 2 horas 
# BodyPlus 200: 2 horas 
prob += 2 * x1 + 2 * x2 <= 140, "Ensamblaje"

# RESTRICCIÓN DE MEZCLA:
# BodyPlus 200 debe ser al menos 25% de la producción total
# x2 >= 0.25 * (x1 + x2)
# x2 >= 0.25*x1 + 0.25*x2
# x2 - 0.25*x2 >= 0.25*x1
# 0.75*x2 >= 0.25*x1
# 3*x2 >= x1  ⟹  x1 - 3*x2 <= 0 
prob += x1 - 3 * x2 <= 0, "Mezcla_25porciento"

print("\n=== RESTRICCIONES ===")
print("Mecanizado: 8*x1 + 12*x2 <= 600")
print("Pintura: 5*x1 + 10*x2 <= 450")
print("Ensamblaje: 2*x1 + 2*x2 <= 140")
print("Mezcla: x1 - 3*x2 <= 0 (x2 >= 25% del total)")

# Resolvemos el problema
print("\n=== RESOLVIENDO ===")
prob.solve()

# Obtenemos los valores de las variables
x1_value = value(x1)
x2_value = value(x2)
total_production = x1_value + x2_value

# Mostramos el estado de la solución
print(f"Estado: {LpStatus[prob.status]}")

# Mostramos los resultados
print("\n=== RESULTADOS ÓPTIMOS ===")
print(f"BodyPlus 100 (x1) = {x1_value:.2f} unidades")
print(f"BodyPlus 200 (x2) = {x2_value:.2f} unidades")
print(f"Producción Total = {total_production:.2f} unidades")
print(f"Utilidad Total = ${value(prob.objective):,.2f}")

# Verificamos el porcentaje de BodyPlus 200
if total_production > 0:
    percentage_x2 = (x2_value / total_production) * 100
    print(f"BodyPlus 200 representa {percentage_x2:.1f}% de la producción")

# Calculamos el uso de cada recurso
mechanized_usage = 8 * x1_value + 12 * x2_value
paint_usage = 5 * x1_value + 10 * x2_value
assembly_usage = 2 * x1_value + 2 * x2_value

print("\n=== USO DE RECURSOS ===")
resources = [
    ("Mecanizado", mechanized_usage, 600),
    ("Pintura", paint_usage, 450),
    ("Ensamblaje", assembly_usage, 140)
]

for name, usage, limit in resources:
    slack = limit - usage
    percentage = (usage / limit) * 100
    print(f"{name}: {usage:.2f}/{limit} horas ({percentage:.1f}%) - Holgura: {slack:.2f}h")

# Análisis de restricciones activas
print("\n=== ANÁLISIS DE RESTRICCIONES ===")
if abs(mechanized_usage - 600) < 0.01:
    print("• Mecanizado: ACTIVA (recurso completamente utilizado)")
else:
    print(f"• Mecanizado: INACTIVA (holgura: {600 - mechanized_usage:.2f}h)")

if abs(paint_usage - 450) < 0.01:
    print("• Pintura: ACTIVA (recurso completamente utilizado)")
else:
    print(f"• Pintura: INACTIVA (holgura: {450 - paint_usage:.2f}h)")

if abs(assembly_usage - 140) < 0.01:
    print("• Ensamblaje: ACTIVA (recurso completamente utilizado)")
else:
    print(f"• Ensamblaje: INACTIVA (holgura: {140 - assembly_usage:.2f}h)")

mix_constraint = x1_value - 3 * x2_value
if abs(mix_constraint) < 0.01:
    print("• Restricción de mezcla: ACTIVA (BodyPlus 200 = exactamente 25%)")
else:
    print(f"• Restricción de mezcla: INACTIVA (BodyPlus 200 > 25%)")

print("\n=== RECOMENDACIÓN GERENCIAL ===")
print(f"Producir {x1_value:.0f} unidades de BodyPlus 100 y {x2_value:.0f} unidades de BodyPlus 200")
print(f"Utilidad esperada: ${value(prob.objective):,.2f}")