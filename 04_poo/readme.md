# Fundamentos de la Programación Orientada a Objetos (POO):

La **Programación Orientada a Objetos (POO)** es un enfoque de desarrollo de software que estructura el programa en torno a **objetos**. Estos objetos representan entidades del mundo real o conceptos abstractos, y son creados a partir de **clases**. Las clases actúan como plantillas que definen las características y comportamientos de los objetos, mediante **atributos** (que almacenan datos) y **métodos** (que realizan acciones).


## Pilares de la Programación Orientada a Objetos

La **POO** se basa en cuatro pilares fundamentales. Estos conceptos han evolucionado con el tiempo y se han adaptado a diferentes lenguajes de programación, pero las bases siguen siendo las mismas:

- **Abstracción**
- **Encapsulamiento**
- **Herencia**
- **Polimorfismo**

## Abstracción

La **abstracción** es el proceso de simplificar un problema o sistema, enfocándose en los aspectos más importantes y relevantes, mientras se ignoran los detalles innecesarios o irrelevantes. En otras palabras, se trata de identificar qué es esencial para definir un objeto y qué no lo es.

### Ejemplo:

Imagina que estás pensando en un **árbol**. Al abstraer un árbol, piensas en sus características esenciales: tiene un tronco, ramas, hojas, raíces, etc. No te preocupas por detalles específicos como la forma exacta de cada hoja o el color exacto del tronco. 

En POO, la abstracción se refiere a tomar estas características clave y plasmarlas en un código que el ordenador pueda entender y utilizar para representar ese objeto.

## Encapsulamiento

El **encapsulamiento** es el principio de ocultar los detalles internos de un objeto y exponer solo lo que es necesario para su uso. Esto se logra protegiendo las propiedades y comportamientos del objeto para evitar que sean modificados de manera inapropiada, ya sea intencionalmente o por error.

### Ejemplo:

Piensa en un **automóvil**. Cuando pisas el acelerador, no necesitas entender todo el complejo proceso mecánico y electrónico que ocurre para que el coche avance. Solo interactúas con el pedal, y el resto está "encapsulado". De la misma manera, en POO, el encapsulamiento permite a los usuarios de un objeto trabajar con él sin tener que entender o interactuar con su complejidad interna.

El encapsulamiento protege a los objetos de cambios no deseados y mantiene la integridad del sistema.

## Herencia

La **herencia** permite crear nuevas clases (o tipos de objetos) basadas en clases existentes, reutilizando y extendiendo su comportamiento. Es una forma de crear jerarquías de clases donde las clases derivadas heredan atributos y métodos de sus clases "padre".

### Ejemplo:

En la naturaleza, los **seres vivos** heredan características de sus antecesores, como el color de piel o la forma de los ojos. En POO, de manera similar, una clase "hija" puede heredar propiedades y métodos de una clase "padre". Esto permite reutilizar código ya existente y agregar nuevas características o comportamientos.

## Polimorfismo

El **polimorfismo** es la capacidad de los objetos de diferentes clases de responder al mismo mensaje o método de diferentes maneras. Es decir, permite que el mismo método se ejecute de forma distinta en diferentes clases.

### Ejemplo:

Considera una interfaz llamada **Animal** que tiene un método `comer()`. Si tienes clases como `Perro` y `Pájaro`, ambas podrían implementar `comer()` de manera diferente, pero desde el punto de vista del código que las utiliza, solo importa que ambos animales saben "comer". Esto permite que se utilice el mismo código para manejar diferentes tipos de objetos sin tener que preocuparse por las diferencias internas entre ellos.

## Resumen

Estos cuatro pilares son esenciales para entender cómo funciona la Programación Orientada a Objetos y cómo se aplican en la práctica para crear sistemas robustos, reutilizables y fáciles de mantener.

## Otros Conceptos Clave:

- **Clase**: Es una plantilla o estructura que define los atributos (datos) y métodos (funciones) que un objeto creado a partir de ella tendrá.
- **Objeto**: Es una instancia específica de una clase, es decir, un ejemplo concreto creado utilizando la definición de una clase.
- **Atributo**: Es una variable definida en una clase o en un objeto que almacena información sobre el estado del objeto.
- **Método**: Es una función definida dentro de una clase o un objeto, que describe el comportamiento o las acciones que el objeto puede realizar.


## Imagina que quieres crear un programa para gestionar una tienda de mascotas.

### Clases:
- **Animal**: Sería la clase más general. Tendría atributos como `nombre`, `edad` y métodos como `comer()` y `dormir()`.
- **Perro**: Hereda de `Animal` y agrega atributos específicos como `raza` y métodos como `ladrar()`.
- **Gato**: También hereda de `Animal` y agrega atributos como `color de ojos` y métodos como `maullar()`.

### Objetos:
- Cada mascota que tengas en tu tienda sería un objeto de una de estas clases. Por ejemplo, un labrador llamado `"Max"` sería un objeto de la clase `Perro`.

### Atributos y métodos:
- `Max` tendría atributos como `nombre="Max"`, `raza="Labrador"`, `edad=3`.
- `Max` podría realizar acciones como `ladrar()` o `comer()`.

### Herencia:
- Al crear la clase `Perro`, no tuvimos que volver a definir los métodos `comer()` y `dormir()`, ya que los heredó de la clase `Animal`.

### Encapsulamiento:
- Puedes ocultar detalles internos de un objeto, como cómo se calcula la edad de un animal. Solo expones los métodos necesarios para interactuar con el objeto.

### Polimorfismo:
- Puedes tratar a un perro y a un gato como si fueran animales, ya que ambos comparten el método `comer()`.

### Resumen:
La POO nos permite modelar el mundo real de una manera más natural y organizada. Al utilizar clases y objetos, podemos crear programas más flexibles, reutilizables y fáciles de mantener.

- **Clase**: Un molde para crear objetos.
- **Objeto**: Una instancia de una clase, como un perro específico.
- **Atributo**: Una característica de un objeto (nombre, edad, etc.).
- **Método**: Una acción que puede realizar un objeto (ladrar, comer, etc.).
- **Herencia**: Cuando una clase hereda características de otra clase.
- **Encapsulamiento**: Ocultar detalles internos de un objeto.
- **Polimorfismo**: Tratar objetos de diferentes clases de forma similar.




