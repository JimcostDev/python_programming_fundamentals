import json
import pandas as pd
import matplotlib.pyplot as plt

# Cargar el dataset desde el archivo JSON
with open('ventas.json', 'r') as f:
  data = json.load(f)

# Crear un DataFrame de pandas
df = pd.DataFrame(data)

# Calcular el total de ventas por producto
df['total_venta'] = df['cantidad'] * df['precio']
ventas_por_producto = df.groupby('producto')['total_venta'].sum()

# Mostrar las ventas por producto
print("Ventas por producto:\n", ventas_por_producto)

# Crear un gráfico de barras de las ventas por producto
plt.figure(figsize=(8, 6))
ventas_por_producto.plot(kind='bar')
plt.title('Total de Ventas por Producto')
plt.xlabel('Producto')
plt.ylabel('Ventas')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Calcular el promedio de precio por producto
promedio_precio_por_producto = df.groupby('producto')['precio'].mean()

# Mostrar el promedio de precio por producto
print("\nPromedio de precio por producto:\n", promedio_precio_por_producto)

# Crear un gráfico de barras del promedio de precio por producto
plt.figure(figsize=(8, 6))
promedio_precio_por_producto.plot(kind='bar')
plt.title('Promedio de Precio por Producto')
plt.xlabel('Producto')
plt.ylabel('Precio Promedio')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()