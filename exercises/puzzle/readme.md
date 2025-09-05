# Resolución del Puzzle de las Losetas

Este documento proporciona una explicación detallada del código para resolver el puzzle de las losetas utilizando Python. El programa permite resolver puzzles de tamaños 2x2, 3x3 y 4x4, determinando si el puzzle tiene solución, mostrando los pasos necesarios para resolverlo y el tiempo tomado para encontrar la solución.

## Estructura del Código

### Importaciones

El código utiliza las siguientes importaciones:

- `heapq`: Permite implementar una cola de prioridad, necesaria para el algoritmo A*.
- `time`: Utilizado para medir el tiempo de ejecución del algoritmo.
- `typing`: Proporciona herramientas para definir tipos de datos en las funciones, mejorando la legibilidad y el mantenimiento del código.

### Clase `Puzzle`

La clase `Puzzle` encapsula toda la lógica necesaria para resolver el puzzle de las losetas. La estructura de la clase es la siguiente:

- **Constructor**: Inicializa el estado inicial del puzzle, su tamaño y el estado meta.
- **Generación del Estado Meta**: Genera el estado objetivo del puzzle donde las losetas están ordenadas y la última posición es la vacía (0).
- **Encontrar la Posición Vacía**: Encuentra la posición de la loseta vacía (0).
- **Verificar Si el Puzzle es Resoluble**: Determina si el puzzle es resoluble contando el número de inversiones en la configuración actual.
- **Heurística (Distancia de Manhattan)**: Calcula la distancia de Manhattan desde el estado actual al estado objetivo. Esta heurística ayuda a priorizar los estados más cercanos a la solución en el algoritmo A*.
- **Obtener Vecinos**: Genera los estados vecinos al mover la loseta vacía en las cuatro direcciones posibles (arriba, abajo, izquierda, derecha).
- **Resolver el Puzzle**: Utiliza el algoritmo A* para encontrar el camino más corto desde el estado inicial al estado objetivo. Si el puzzle no es resoluble, lo indica. Si no encuentra una solución alcanzable, también lo indica.

### Funciones Auxiliares

El código también incluye algunas funciones auxiliares:

- **Mostrar Menú**: Permite al usuario seleccionar el tamaño del puzzle a resolver.
- **Obtener Tablero**: Solicita al usuario que ingrese la configuración inicial del puzzle según el tamaño seleccionado.

### Verificar Si el Puzzle es Resoluble
Para determinar si un puzzle es resoluble, se cuenta el número de inversiones en la configuración actual del puzzle. Una inversión ocurre cuando un número menor aparece después de un número mayor en la configuración del puzzle, tomando como referencia el orden de los números de izquierda a derecha y de arriba hacia abajo, incluyendo la casilla vacía como el número mayor (en el caso del puzzle resuelto).

Por ejemplo, en el puzzle resuelto:
```
1 2
3 0
```

No hay inversiones porque todos los números aparecen en orden ascendente. Sin embargo, en un puzzle no resuelto, como el siguiente:

```
2 1
3 0
```
Hay una inversión porque el número `1` aparece antes del número `2`.

Si el número de inversiones en la configuración actual es par, el puzzle es resoluble. Si es impar, el puzzle no es resoluble.

Este método se basa en el hecho de que en cada movimiento de loseta, el número de inversiones en el puzzle cambia en un número par. Por lo tanto, si el número de inversiones en la configuración inicial y en la configuración objetivo tienen la misma paridad, el puzzle es resoluble, ya que se puede llegar de una configuración a la otra con un número par de movimientos. Si tienen paridades diferentes, el puzzle no es resoluble.


## Ejemplo de uso:

```sh
Seleccione el tamaño del puzzle que desea resolver:
1. Puzzle 2x2
2. Puzzle 3x3
3. Puzzle 4x4
Ingrese el número de su opción: 1

Ingrese la fila 1 de 2, separando los números con espacios: 1 2
Ingrese la fila 2 de 2, separando los números con espacios: 0 3
```