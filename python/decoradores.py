# Los decoradores en Python son funciones que modifican o
# extienden el comportamiento de otras funciones/métodos, 
# sin alterar su código original. Son muy útiles para 
# reutilizar lógica común (ej: validación, logging, timing).

#Ejemplo Base: Decorador Simple
print("\nEjemplo Base: Decorador Simple")
def decorador_base(func):
    def wrapper():
        print("--- Antes de ejecutar la función ---")
        func()  # Llama a la función original
        print("--- Después de ejecutar la función ---")
    return wrapper

@decorador_base
def saludar():
    print("¡Hola Mundo!")

# Al llamar a la función, se aplica el decorador
saludar()

# Decorador con Argumentos
print("\nDecorador con Argumentos")
def decorador(func):
    def envoltura(*args, **kwargs):
        print("Ejecutando función...")
        resultado = func(*args, **kwargs)
        print("Ejecución finalizada")
        return resultado
    return envoltura

@decorador
def suma(a, b):
    return a + b

print(suma(3, 5))

# Decorador integrados en Python
print("\nDecorador integrados en Python")
class Persona:
    def __init__(self, nombre):
        self._nombre = nombre

    @property
    def nombre(self):
        return self._nombre

p = Persona("Ronaldo")
print(p.nombre)  # Se accede como atributo, no como método


# Ejemplo Práctico: Medir Tiempo de Ejecución
print("\nEjemplo Práctico: Medir Tiempo de Ejecución")
import time
from functools import wraps

def medir_tiempo(func):
    @wraps(func)  # Preserva los metadatos de la función original
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = func(*args, **kwargs)  # Ejecuta la función
        fin = time.time()
        print(f"{func.__name__} tardó {fin - inicio:.4f} segundos")
        return resultado
    return wrapper

@medir_tiempo
def factorial(n: int) -> int:
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Probamos el decorador
print(factorial(5))  # 120