# Creación de Algoritmos

En esta sección aprenderemos cómo crear algoritmos, desde la identificación del problema hasta su implementación en un lenguaje de programación. Además, exploraremos los tipos de datos y operadores básicos utilizados en programación.

## Contenido

1. [Metodología para la creación de algoritmos](#1-metodología-para-la-creación-de-algoritmos)
2. [Tipos de datos](#2-tipos-de-datos)
3. [Tipos de operadores](#3-tipos-de-operadores)

---

## 1. Metodología para la creación de algoritmos

### Definición

Cuando un programador se enfrenta a un problema específico, su tarea es encontrar una solución y expresarla mediante un algoritmo. Este algoritmo luego debe codificarse en un lenguaje de programación específico, para finalmente ejecutarlo en una computadora y obtener una solución al problema planteado.

### Etapas de desarrollo

1. **Análisis**: Identificar las entradas (datos iniciales), el proceso (acciones a realizar con los datos) y las salidas (resultado esperado).
2. **Diseño**: Utilización de herramientas como pseudocódigo o diagramas de flujo para plasmar el análisis previamente realizado.
3. **Implementación**: Utilizar un lenguaje de programación y un entorno de desarrollo para crear el programa o software que resuelve el problema.

> **Reto**:  
> Tres amigos deciden tomar un café. La cuenta asciende a $25 por los tres cafés. Cada uno pone $10, lo que suma $30 en total. El camarero les devuelve $5, de los cuales cada uno toma $1, y los $2 restantes se quedan como propina. Es decir, cada uno paga $9, lo que suma $27, más los $2 de la propina, suman $29. **¿Dónde está el dólar que falta?**
> 
> **Solución**: El error radica en la confusión con la suma de los valores. Cada persona paga $9, que suman $27, y de esos $27, $25 corresponden a los cafés y $2 a la propina. No hay ningún dólar perdido; el cálculo se está haciendo de manera incorrecta al intentar sumar los $2 de propina.

---

## 2. Tipos de datos

Un **dato** es la información que se manipula dentro de un programa. Una **variable** es un espacio en la memoria que almacena un dato y cuyo valor puede cambiar durante la ejecución del programa.

> Nota: Cada lenguaje de programación puede manejar tipos de datos de manera diferente, pero los conceptos fundamentales son los mismos.

### Principales tipos de datos:

1. **Texto**
2. **Numéricos**
3. **Lógicos o Booleanos**
4. **Colecciones de datos**

### Representación de texto:

- **Caracteres (char)**: Representan un único carácter, como una letra, número (texto), símbolo o emoji.
- **Cadenas de caracteres (string)**: Secuencias de caracteres que forman palabras o frases.

### Numéricos:

- **Enteros (int)**: Representan números sin decimales, ya sean positivos o negativos.
- **Reales (float, double)**: Representan números con decimales. La diferencia entre `float` y `double` radica en la precisión con la que manejan los valores.

### Lógicos o Booleanos:

- **Booleanos (bool)**: Representan un valor lógico, que puede ser verdadero (`true`) o falso (`false`).

### Colecciones de datos:

- **Arreglos (arrays)**: Colecciones de elementos del mismo tipo que se almacenan en posiciones consecutivas de memoria.
- **Listas (list)**: Colecciones ordenadas de elementos que pueden ser de distintos tipos de datos.
- **Estructuras (structs)**: Permiten crear tipos de datos personalizados que contienen múltiples campos con diferentes tipos de datos.

---

## 3. Tipos de operadores

Los **operadores** son símbolos o palabras que se utilizan para realizar operaciones sobre uno o más operandos (valores o variables).

### 1. Operadores aritméticos

Se utilizan para realizar operaciones matemáticas en expresiones numéricas.

- **Suma (+)**: Suma dos valores o concatena cadenas (dependiendo del lenguaje).
- **Resta (-)**: Resta un valor de otro.
- **Multiplicación (*)**: Multiplica dos valores.
- **División (/)**: Divide un valor por otro.
- **Módulo (%)**: Devuelve el resto de la división de dos números.
- **Incremento (++)**: Aumenta el valor de una variable en uno (no en todos los lenguajes).
- **Decremento (--)**: Disminuye el valor de una variable en uno (no en todos los lenguajes).

### 2. Operadores lógicos

Evalúan condiciones lógicas y devuelven un valor booleano (verdadero o falso). Son fundamentales en la toma de decisiones.

- **AND lógico (&&)**: Devuelve verdadero si ambas condiciones son verdaderas.
- **OR lógico (||)**: Devuelve verdadero si al menos una de las condiciones es verdadera.
- **NOT lógico (!)**: Invierte el valor lógico de una condición.

### 3. Operadores de comparación

Comparan dos valores y devuelven un valor booleano (verdadero o falso).

- **Igualdad (==)**: Verifica si dos valores son iguales.
- **Desigualdad (!=)**: Verifica si dos valores son diferentes.
- **Mayor que (>)**: Verifica si un valor es mayor que otro.
- **Mayor o igual que (>=)**: Verifica si un valor es mayor o igual que otro.
- **Menor que (<)**: Verifica si un valor es menor que otro.
- **Menor o igual que (<=)**: Verifica si un valor es menor o igual que otro.

---

> **Reto**:  
> Investigar sobre:
> 1. ¿Qué es una constante y en qué se diferencia de una variable?
> 2. ¿Qué son las estructuras de control y para qué se usan?

Para más información, visita [jimcostdev.com](http://jimcostdev.com).