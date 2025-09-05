# Los algoritmos de ordenamiento y su tiempo

En pocas palabras, la complejidad temporal nos dice **cuántos pasos** necesita un algoritmo para ordenar una lista, 
dependiendo de cuántos elementos tenga la lista. No se trata de medir el tiempo en segundos, sino de entender 
cómo **cambia el tiempo** a medida que aumenta la cantidad de datos.

## ¿Por qué es importante?

La complejidad temporal nos ayuda a **elegir el mejor algoritmo** para ordenar una lista. 
Imaginemos dos algoritmos: uno que ordena una lista de 10 elementos en 1 segundo y otro que lo 
hace en 2 segundos. Si la lista tiene 1000 elementos, el primer algoritmo podría tardar 100 segundos,
mientras que el segundo podría tardar 2000. ¡En este caso, el primer algoritmo sería mucho más eficiente!

## Tres casos a considerar:

- **Mejor caso:** El algoritmo ordena la lista de la forma más rápida posible.
- **Peor caso:** El algoritmo tarda más tiempo en ordenar la lista.
- **Caso promedio:** El tiempo que tarda el algoritmo en ordenar la lista se calcula en promedio, considerando diferentes tipos de listas.

## En resumen:

- La complejidad temporal nos habla de la **eficiencia** de un algoritmo de ordenamiento.
- analiza en función del **tamaño de la lista (n).**
- Hay que considerar el mejor caso, el peor caso y el caso promedio.

## Complejidad temporal de algoritmos comunes: 

| Algoritmo   | Mejor caso | Peor caso | Caso promedio |
|-------------|------------|-----------|----------------|
| Merge Sort  | O(n log n) | O(n log n) | O(n log n)     |
| QuickSort   | O(n log n) | O(n^2)     | O(n log n)     |
| Burbuja     | O(n)       | O(n^2)     | O(n^2)         |
| Inserción   | O(n)       | O(n^2)     | O(n^2)         |
| Selección   | O(n^2)     | O(n^2)     | O(n^2)         |

## Explicación de la notación:

- O(n): El tiempo de ejecución aumenta linealmente con el tamaño de la lista.
- O(n log n): El tiempo de ejecución aumenta logarítmicamente con el tamaño de la lista.
- O(n^2): El tiempo de ejecución aumenta cuadráticamente con el tamaño de la lista.

## Conclusión:

- Merge Sort y QuickSort son los algoritmos más eficientes en la mayoría de los casos.
- Burbuja, Inserción y Selección son menos eficientes, especialmente con grandes conjuntos de datos.

## Consideraciones adicionales:

- La complejidad temporal es solo una medida de la eficiencia del algoritmo.
- Otros factores, como la memoria utilizada o la facilidad de implementación, también pueden ser importantes.
- En algunos casos, un algoritmo menos eficiente puede ser más adecuado para una tarea específica.

