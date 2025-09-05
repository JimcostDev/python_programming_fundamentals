class Pila:
    def __init__(self):
        self.pila = []

    def crear(self):
        self.pila = []

    def apilar(self, elemento):
        self.pila.append(elemento)

    def desapilar(self):
        if not self.esta_vacia():
            return self.pila.pop()
        else:
            return None

    def esta_vacia(self):
        return len(self.pila) == 0
    
    def imprimir_resultados(self):
        if not self.esta_vacia():
            print("Elementos de la pila:", self.pila)
        else:
            print("La pila está vacía")

    def modificar_estructura(self, x):
        while not self.esta_vacia() and self.pila[-1] != x:
            self.desapilar()

        if not self.esta_vacia():
            print(f"Encontrado {x}, eliminando elementos previos...")
            while len(self.pila) > 1:
                self.desapilar()
        else:
            print(f"No se encontró {x} en la estructura")

        print(f"Estado final de la pila:")
        self.imprimir_resultados()


class Cola:
    def __init__(self):
        self.cola = []

    def crear(self):
        self.cola = []

    def encolar(self, elemento):
        self.cola.append(elemento)

    def desencolar(self):
        if not self.esta_vacia():
            return self.cola.pop(0)
        else:
            return None

    def esta_vacia(self):
        return len(self.cola) == 0

    def imprimir_resultados(self):
        if not self.esta_vacia():
            print("Elementos de la cola:", self.cola)
        else:
            print("La cola está vacía")

    def modificar_estructura(self, x):
        while not self.esta_vacia() and self.cola[0] != x:
            self.desencolar()

        if not self.esta_vacia():
            print(f"Encontrado {x}, eliminando elementos previos...")
            while len(self.cola) > 1:
                self.desencolar()
        else:
            print(f"No se encontró {x} en la estructura")

        print(f"Estado final de la cola:")
        self.imprimir_resultados()


def main():
    pila = Pila()
    cola = Cola()

    while True:
        print("-" * 20)
        print("1. Apilar un elemento")
        print("2. Desapilar un elemento")
        print("3. Encolar un elemento")
        print("4. Desencolar un elemento")
        print("5. Modificar estructura")
        print("6. Salir")
        print("-" * 20)

        opcion = int(input("Seleccione una opción: "))

        if opcion == 1:
            elemento = input("Ingrese un elemento: ")
            pila.apilar(elemento)
            print(f"Elemento {elemento} apilado correctamente")
            pila.imprimir_resultados()

        elif opcion == 2:
            elemento = pila.desapilar()
            if elemento is not None:
                print(f"Elemento {elemento} desapilado correctamente")
            else:
                print("La pila está vacía")
            pila.imprimir_resultados()

        elif opcion == 3:
            elemento = input("Ingrese un elemento: ")
            cola.encolar(elemento)
            print(f"Elemento {elemento} encolado correctamente")
            cola.imprimir_resultados()

        elif opcion == 4:
            elemento = cola.desencolar()
            if elemento is not None:
                print(f"Elemento {elemento} desencolado correctamente")
            else:
                print("La cola está vacía")
            cola.imprimir_resultados()

        elif opcion == 5:
            estructura = input("Seleccione la estructura (Pila/Cola): ")
            x = input("Ingrese el valor X a buscar: ")
            if estructura.lower() == "pila":
                pila.modificar_estructura(x)
            elif estructura.lower() == "cola":
                cola.modificar_estructura(x)
            else:
                print("Estructura no válida")

        elif opcion == 6:
            break

        else:
            print("Opción no válida")


if __name__ == "__main__":
    main()
