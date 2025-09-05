## Pilas:
Imagina una pila de libros. Puedes agregar libros uno encima del otro y también quitar el libro que está en la parte superior de la pila. Esta estructura de datos funciona de la misma manera. En una pila, solo puedes agregar elementos (llamado "push") en la parte superior de la pila y solo puedes sacar elementos de la parte superior (llamado "pop"). Es decir, el último elemento en entrar es el primero en salir (LIFO: Last In, First Out). Por ejemplo, si tienes una pila de números (1, 2, 3), para sacar el número 3, primero tendrías que sacar el número 2 y luego el número 1.

## Colas:
Ahora, imagina una fila en un supermercado. Las personas se ponen en la fila desde el final y salen por el frente. Esta estructura de datos es similar. En una cola, puedes agregar elementos al final de la fila (llamado "enqueue") y sacar elementos del frente de la fila (llamado "dequeue"). Es decir, el primer elemento en entrar es el primero en salir (FIFO: First In, First Out). Por ejemplo, si tienes una cola de números (1, 2, 3), para sacar el número 1, lo sacarías primero, luego el número 2 y finalmente el número 3.

## Documentación Técnica - Estructuras de Datos (Pila y Cola) en Python

---

**Descripción:**
Este código implementa las estructuras de datos de Pila (Stack) y Cola (Queue) en Python, junto con algunas operaciones básicas como apilar, desapilar, encolar y desencolar. Además, proporciona una función para modificar la estructura de la pila o la cola eliminando elementos hasta encontrar un valor específico.

---

**Clases:**
1. **Pila (Stack):**
   - **Métodos:**
     - `__init__(self)`: Constructor de la clase.
     - `crear(self)`: Método para vaciar la pila.
     - `apilar(self, elemento)`: Método para agregar un elemento a la pila.
     - `desapilar(self)`: Método para eliminar y devolver el elemento en la parte superior de la pila.
     - `esta_vacia(self)`: Método para verificar si la pila está vacía.
     - `imprimir(self)`: Método para imprimir los elementos de la pila.

2. **Cola (Queue):**
   - **Métodos:**
     - `__init__(self)`: Constructor de la clase.
     - `crear(self)`: Método para vaciar la cola.
     - `encolar(self, elemento)`: Método para agregar un elemento a la cola.
     - `desencolar(self)`: Método para eliminar y devolver el elemento en el frente de la cola.
     - `esta_vacia(self)`: Método para verificar si la cola está vacía.
     - `imprimir(self)`: Método para imprimir los elementos de la cola.

---

**Funciones:**
1. `modificar_estructura(estructura, x)`: Función que modifica la estructura (pila o cola) eliminando elementos hasta encontrar un valor específico `x`.

2. `main()`: Función principal que crea instancias de Pila y Cola, y proporciona un menú interactivo para realizar operaciones en estas estructuras.

---

**Uso:**
1. Ejecuta el script.
2. Selecciona la operación deseada del menú.
3. Ingresa los elementos según corresponda.


