# Encontrar el Par de Puntos Más Cercano

Este proyecto implementa un algoritmo eficiente para encontrar el par de puntos más cercano en un plano cartesiano utilizando el algoritmo de Divide y Vencerás. Este tipo de algoritmo es más eficiente que la comparación de todos los pares de puntos posibles.

## Conceptos Clave

### Distancia Euclidiana

La distancia euclidiana es una medida de la distancia recta entre dos puntos en un espacio euclidiano. En un plano cartesiano de dos dimensiones, se calcula con la fórmula:

\[ d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2} \]

donde \( (x_1, y_1) \) y \( (x_2, y_2) \) son las coordenadas de los dos puntos.

### Algoritmo de Divide y Vencerás

El algoritmo de Divide y Vencerás es una técnica algorítmica que divide un problema en subproblemas más pequeños, resuelve cada subproblema de manera recursiva y luego combina las soluciones de los subproblemas para resolver el problema original. En este contexto, el algoritmo se utiliza para encontrar el par de puntos más cercano de manera eficiente.

## Archivos

El proyecto se basa en tres archivos de datos que contienen coordenadas de puntos en un plano cartesiano:

- `datos_100.txt`
- `datos_1000.txt`
- `datos_10000.txt`

Cada archivo contiene coordenadas en formato `x,y`, separados por comas.

## Funciones Principales

### `distancia_euclidiana(punto1, punto2)`

Calcula la distancia euclidiana entre dos puntos en un plano cartesiano. Esta función toma dos puntos representados como tuplas de coordenadas (x, y) y devuelve la distancia entre ellos.

### `encontrar_par_cercano_en_franja(franja, mejor_distancia)`

Encuentra el par de puntos más cercano dentro de una franja vertical. La franja es una lista de puntos ordenados por su coordenada y. La función compara cada punto con los siguientes hasta 7 puntos (debido a una propiedad del problema que garantiza que no es necesario comparar más allá de eso para encontrar el par más cercano).

### `obtener_par_mas_cercano_recursivo(puntos_ordenados_x)`

Función recursiva que divide los puntos en mitades para encontrar el par más cercano. Divide la lista de puntos en dos mitades, encuentra el par más cercano en cada mitad recursivamente y luego combina los resultados para encontrar el par más cercano en la franja central.

### `obtener_par_mas_cercano(puntos)`

Función principal que inicia el proceso de búsqueda del par de puntos más cercano. Prepara la lista de puntos ordenándolos por la coordenada x y llama a la función recursiva `obtener_par_mas_cercano_recursivo`.

### `leer_archivo(archivo)`

Lee un archivo de texto que contiene las coordenadas de los puntos y devuelve una lista de tuplas con las coordenadas.

### `procesar_archivo(archivo)`

Procesa un archivo de puntos, encuentra el par más cercano y mide el tiempo de ejecución. Lee los puntos del archivo, encuentra el par más cercano y muestra los resultados.

### `main()`

Función principal del programa que procesa los tres archivos de puntos y muestra los resultados por separado.

## Ejecución del Programa

Para ejecutar el programa, asegúrate de tener los archivos de datos en el mismo directorio que el script y ejecuta el script:

```sh
python par_mas_cercano.py
```

### Dependencias
```sh
pip install pylint
```


