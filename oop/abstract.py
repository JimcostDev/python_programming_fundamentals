"""
En Python, una clase abstracta es un tipo especial de clase que sirve 
como plantilla para otras clases, pero que no puede ser instanciada directamente. 
Es decir, no puedes crear objetos a partir de una clase abstracta. 
Su propósito principal es definir una interfaz común que las subclases deben implementar.
"""
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def hacer_sonido(self):
        pass

class Perro(Animal):
    def hacer_sonido(self):
        print("Guau!")

class Gato(Animal):
    def hacer_sonido(self):
        print("Miau!")

# Intentar crear un objeto de la clase Animal dará un error:
# animal = Animal()  # TypeError: Can't instantiate abstract class Animal with abstract methods hacer_sonido