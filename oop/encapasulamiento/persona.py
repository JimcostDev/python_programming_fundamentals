"""
Ejemplo de una clase Persona, se explica el concepto de encapsulamiento y 
cómo se pueden definir métodos para acceder y modificar los atributos de la clase.

Getters y Setters (encapsulamiento):
Métodos clásicos en la programación orientada a objetos. Estos Getters y Setters permite 
asignarles valores a esos atributos y obtener los valores de esos atributos.
"""

class Persona:
    def __init__(self, nombre="", edad=0, peso=0.0, estatura=0.0):
        self.__nombre = nombre
        self.__edad = edad
        self.__peso = peso
        self.__estatura = estatura

    # Getters
    def get_nombre(self):
        return self.__nombre

    def get_edad(self):
        return self.__edad

    def get_peso(self):
        return self.__peso

    def get_estatura(self):
        return self.__estatura

    # Setters
    def set_nombre(self, nombre):
        if not nombre or len(nombre) <= 1:
            print("El nombre no puede ser vacío o muy corto")
        else:
            self.__nombre = nombre

    def set_edad(self, edad):
        if edad < 0 or edad > 150:
            print("La edad no es válida")
        else:
            self.__edad = edad

    def set_peso(self, peso):
        if peso < 0 or peso > 300:
            print("El peso no es válido")
        else:
            self.__peso = peso

    def set_estatura(self, estatura):
        if estatura < 0 or estatura > 3.0:
            print("La estatura no es válida")
        else:
            self.__estatura = estatura

    def saludar(self):
        print(f"Hola, mi nombre es: {self.__nombre}")
