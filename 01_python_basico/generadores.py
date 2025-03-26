# Los generadores en Python son una forma sencilla de crear iteradores.
# Se utilizan para crear secuencias de valores que se pueden iterar, pero no se almacenan en la memoria. 
# En lugar de almacenar todos los valores en la memoria, los generadores generan los valores sobre la marcha.

# Ventajas:
# -Lazy evaluation: Los valores se generan bajo demanda.
# -Sin almacenamiento: No ocupa memoria para guardar toda la secuencia.

# Características principales:
# - Se definen con la palabra clave yield en lugar de return.
# - Se pueden iterar con un bucle for o usar la función next().
# - Eficientes en términos de memoria y rendimiento.

print("Generadores:")
print("Ejemplo 1:")
def contador(n):
    for x in range(n):
        yield x # yield devuelve el valor y pausa la ejecución de la función
        
gen = contador(5)
print(next(gen)) # 0
print(next(gen)) # 1
print(next(gen)) # 2
print(next(gen)) # 3
print(next(gen)) # 4

# se pude hacer con un for
for num in contador(3):
    print(num) # 0, 1, 2


print("Ejemplo 2:")
# Si un generador necesita delegar parte de su trabajo a otro iterable, se puede usar yield from
def generador():
    yield from [1, 2, 3]  # Equivalente a hacer yield en cada elemento

for num in generador():
    print(num)  # Imprime 1, 2, 3
    
# Ejemplo 3: Procesar un archivo de registros (logs) muy grande
print("Ejemplo 3:")
def leer_logs(ruta_archivo):
    with open(ruta_archivo, 'r') as archivo:
        for linea in archivo:
            # Yield permite procesar línea por línea sin cargar todo el archivo
            yield linea.strip()

def filtrar_errores(ruta_archivo, palabra_clave):
    generador_lineas = leer_logs(ruta_archivo)
    for linea in generador_lineas:
        if palabra_clave in linea:
            yield linea

# Uso del generador
ruta = 'servidor.log'
palabra_clave = 'ERROR'

# Procesa línea a línea, consumiendo poca memoria
for error in filtrar_errores(ruta, palabra_clave):
    print(f"Error detectado: {error}")

# Los generadores son muy útiles en tareas como procesamiento de archivos grandes, manipulación de datos en streaming y generación de secuencias infinitas.