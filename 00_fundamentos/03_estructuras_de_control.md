# Estructuras de Control

Las **estructuras de control** son componentes esenciales en la programación, ya que permiten alterar el flujo normal de ejecución de un programa, permitiendo tomar decisiones y realizar repeticiones controladas de ciertas acciones. Esto permite crear programas más flexibles, eficientes y capaces de adaptarse a diferentes situaciones.

---

## Contenido

- [Estructuras de Control](#estructuras-de-control)
  - [Contenido](#contenido)
  - [¿Qué son las estructuras de control?](#qué-son-las-estructuras-de-control)
  - [Estructuras de selección](#estructuras-de-selección)
    - [Condicional simple](#condicional-simple)
    - [Condicional compuesto](#condicional-compuesto)
    - [Condicional múltiple](#condicional-múltiple)
  - [Estructuras de repetición o bucles](#estructuras-de-repetición-o-bucles)
    - [Bucle `for`](#bucle-for)
    - [Bucle `while`](#bucle-while)
    - [Diferencias entre `for` y `while`](#diferencias-entre-for-y-while)
    - [Bucle infinito](#bucle-infinito)
  - [Reto de investigación](#reto-de-investigación)

---

## ¿Qué son las estructuras de control?

Las **estructuras de control** permiten cambiar el flujo de ejecución de un programa. Sin ellas, las instrucciones se ejecutarían de manera secuencial, una tras otra. Existen dos grandes categorías de estructuras de control:

1. **Estructuras de selección**: Permiten ejecutar diferentes bloques de código dependiendo de si una condición es verdadera o falsa.
2. **Estructuras de repetición o bucles**: Permiten repetir un bloque de código varias veces hasta que se cumpla una condición.

> **Reto**: Imagina un programa que debe determinar si un número es positivo, negativo o cero. Define el proceso y las estructuras de control que usarías para resolver este problema.

---

## Estructuras de selección

Las **estructuras de selección** permiten tomar decisiones dentro de un programa. A partir de una condición, el programa puede ejecutar un bloque de código u otro. Este tipo de estructura es útil para manejar situaciones donde el comportamiento del programa depende de ciertos datos o situaciones.

### Condicional simple

El **condicional simple** evalúa una condición. Si la condición es verdadera, ejecuta un conjunto de instrucciones. Si es falsa, no realiza ninguna acción.

- **Ejemplo**: Verificar si una persona es mayor de edad.

### Condicional compuesto

El **condicional compuesto** añade una segunda opción que se ejecuta cuando la condición no se cumple. Así, se pueden manejar dos posibles resultados: cuando la condición es verdadera o cuando es falsa.

- **Ejemplo**: Verificar si una persona es mayor de edad, y si no lo es, indicar que es menor.

### Condicional múltiple

El **condicional múltiple** permite evaluar varias condiciones de forma secuencial. Si la primera condición es verdadera, se ejecuta el bloque correspondiente. Si no, se evalúa la siguiente condición, y así sucesivamente.

- **Ejemplo**: Asignar una calificación según la nota de un estudiante: "A" para notas superiores a 9, "B" para notas entre 8 y 9, etc.

---

## Estructuras de repetición o bucles

Las **estructuras de repetición**, también conocidas como bucles, permiten ejecutar un bloque de código varias veces de manera continua, hasta que se cumpla o no una determinada condición. Son útiles para automatizar tareas repetitivas.

### Bucle `for`

El **bucle `for`** se utiliza para iterar sobre una secuencia de elementos, como una lista o un rango de números. Es ideal cuando se sabe de antemano cuántas veces se debe repetir el ciclo.

- **Ejemplo**: Iterar sobre una lista de números para imprimir cada uno de ellos.

### Bucle `while`

El **bucle `while`** repite un bloque de código mientras se cumpla una condición específica. A diferencia del bucle `for`, el bucle `while` no requiere saber de antemano el número de repeticiones, ya que la repetición depende de la condición evaluada en cada iteración.

- **Ejemplo**: Continuar pidiendo una contraseña hasta que el usuario ingrese la correcta.

### Diferencias entre `for` y `while`

- **Bucle `for`**: Es utilizado cuando se conoce el número exacto de iteraciones o se itera sobre una colección de elementos.
- **Bucle `while`**: Es utilizado cuando el número de iteraciones no se conoce de antemano y se basa en la evaluación de una condición en cada iteración.

### Bucle infinito

Un **bucle infinito** es un ciclo que nunca termina porque la condición de salida nunca se cumple. En general, es un error de programación, aunque puede ser útil en casos específicos como la ejecución de servicios en segundo plano.

- **Ejemplo**: Un programa que monitorea el estado de un sistema continuamente.

---

## Reto de investigación

> **Reto**: Investiga y describe los siguientes conceptos:
> 
> 1. ¿Qué es un "switch" o "caso" y cómo se diferencia de una estructura condicional simple?
> 2. ¿Qué es la recursividad y cómo se diferencia de un bucle?
> 3. Da ejemplos prácticos donde el uso de bucles es más eficiente que el de estructuras condicionales.

---

Para más información, visita [jimcostdev.com](http://jimcostdev.com).
