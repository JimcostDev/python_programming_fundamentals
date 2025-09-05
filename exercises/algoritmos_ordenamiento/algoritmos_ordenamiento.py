import json
import time
ruta = "./Entrada-800.txt"

# función que retorna el contenido del archivo proporcionado
def leer_archivo():
    archivo = open(ruta, "r")
    contenido = archivo.read()
    archivo.close()
    return contenido

# función que convierte una cadena de caracteres a numeros (retorna una array o lista)
def convertir_str_numero(cadena):
    # dividir la cadena en líneas separadas (se crea una lista o array)
    lineas = cadena.split("\n") 
    lista_numeros = []
    for num in range(len(lineas)):
        lista_numeros.append(int(lineas[num])) #llenar lista con numeros enteros
    return lista_numeros

# función de ordenamiento burbuja
def ordenar_burbuja(a):
  # Código método Burbuja
  for recorrido in range(len(a) - 1):  # recorridos
    for elemento in range(len(a) - 1):  # elementos del arreglo
      if a[elemento] > a[elemento + 1]:
        # cambiar de posicion los numeros (ordenar)
        t = a[elemento]
        a[elemento] = a[elemento + 1]
        a[elemento + 1] = t
  return a

# función de ordenamiento por selección
def ordenar_seleccion(a):
    # Recorrer la lista de elementos
    for num in range(len(a)):
        # Encontrar el elemento más pequeño en el resto de la lista
        min_idx = num
        for menor in range(num+1, len(a)):
            if a[menor] < a[min_idx]:
                min_idx = menor
        # Intercambiar el elemento actual con el más pequeño encontrado
        a[num], a[min_idx] = a[min_idx], a[num]
    return a

# Función de ordenamiento por inserción
def ordenar_insercion(a):
  for i in range(1, len(a)):
    actual = a[i]
    j = i - 1
    while j >= 0 and a[j] > actual:
      a[j + 1] = a[j]
      j -= 1
    a[j + 1] = actual
  return a

# función de ordenamiento por mezcla (Merge Sort)
def merge_sort(a):
  if len(a) <= 1:
    return a
  medio = len(a) // 2
  izquierda = merge_sort(a[:medio])
  derecha = merge_sort(a[medio:])
  return merge(izquierda, derecha)

def merge(izquierda, derecha):
  resultado = []
  i = 0
  j = 0
  while i < len(izquierda) and j < len(derecha):
    if izquierda[i] < derecha[j]:
      resultado.append(izquierda[i])
      i += 1
    else:
      resultado.append(derecha[j])
      j += 1
  resultado += izquierda[i:]
  resultado += derecha[j:]
  return resultado

# función de ordenamiento rápido (Quick Sort)
def quicksort(a):
    if len(a) <= 1:
        return a
    else:
        pivote = a[len(a) - 1]
        menores = [x for x in a if x < pivote]
        iguales = [x for x in a if x == pivote]
        mayores = [x for x in a if x > pivote]
        return quicksort(menores) + iguales + quicksort(mayores)

try:
    def ejecutar_ordenamiento(opcion, array):
        # Inicio del tiempo de ejecución
        inicio = time.time()

        # Seleccionar el algoritmo de ordenamiento
        if opcion == 1:
            lista_ordenada = ordenar_burbuja(array)
            metodo = "Burbuja"
        elif opcion == 2:
            lista_ordenada = ordenar_seleccion(array)
            metodo = "Selección"
        elif opcion == 3:
            lista_ordenada = ordenar_insercion(array)
            metodo = "Inserción"
        elif opcion == 4:
            lista_ordenada = merge_sort(array)
            metodo = "Mezcla (Merge Sort)"
        elif opcion == 5:
            lista_ordenada = quicksort(array)
            metodo = "Rápido (Quick Sort)"
        else:
            print("Ingresa un número entre 1 y 5.")
            return
        # Fin del tiempo de ejecución
        fin = time.time()
        # Duración de la ejecución
        duracion = fin - inicio
        # Mostrar resultados
        print(f"VER RESULTADOS POR {metodo}:")
        print(json.dumps(lista_ordenada, indent=4))
        print(f"El tiempo de ejecución es: {round(duracion, 2)} segundos")

    # EJECUCIÓN DEL ALGORITMO
    opcion = int(input("""POR FAVOR ELIGE EL TIPO DE ORDENAMIENTO QUE QUIERES EJECUTAR:
    1. Ordenamiento Burbuja
    2. Ordenamiento por Selección
    3. Ordenamiento por Inserción
    4. Ordenamiento por Mezcla (Merge Sort)
    5. Ordenamiento Rápido (Quick Sort)

    Escribe aquí tu elección: """))


    cadena = leer_archivo()
    array = convertir_str_numero(cadena)
    ejecutar_ordenamiento(opcion, array)

except ValueError:
    print("Opción no válida. Debe ser un número.")
