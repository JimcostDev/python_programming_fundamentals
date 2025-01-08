"""
 Un protocolo en programación orientada a objetos es como una interfaz bien definida.
 
 Un protocolo sería como un plano arquitectónico que detalla la
 estructura básica de la casa: cuántas habitaciones debe tener, 
 dónde deben ir las ventanas, etc. Cualquier constructor que quiera 
 construir una casa siguiendo ese plano debe asegurarse de que su 
 construcción cumpla con todas las especificaciones del plano.
"""

from dataclasses import dataclass
from typing import Protocol

class Shape(Protocol):
    def area(self) -> float:
        """Calcula el área de la figura."""
        ...
    def perimeter(self) -> float:
        """Calcula el perímetro de la figura."""
        ...

@dataclass
class Circle(Shape):
    radius: float

    def area(self) -> float:
        return 3.14159 * self.radius**2

    def perimeter(self) -> float:
        return 2 * 3.14159 * self.radius

@dataclass
class Square(Shape):
    side: float

    def area(self) -> float:
        return self.side ** 2

    def perimeter(self) -> float:
        return 4 * self.side

def print_shape_info(shape: Shape):
    print(f"Área: {shape.area()}")
    print(f"Perímetro: {shape.perimeter()}")

# Usando las clases
circle = Circle(5)
square = Square(3)

print_shape_info(circle)
print_shape_info(square)