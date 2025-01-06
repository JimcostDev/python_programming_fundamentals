# ejemplo sin usar dataclass
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __repr__(self):
        return f"Persona(nombre='{self.nombre}', edad={self.edad})"

persona1 = Persona("Juan", 30)
print(persona1)  # Salida: Persona(nombre='Juan', edad=30)

# ejemplo usando dataclass
from dataclasses import dataclass

@dataclass
class Persona:
    nombre: str
    edad: int

persona2 = Persona("Pau", 25)
print(persona2)  # Salida: Persona(nombre='Pau', edad=25)