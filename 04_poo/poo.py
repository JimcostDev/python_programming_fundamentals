# Clase base general para todos los animales
class Animal:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def comer(self):
        print(f"{self.nombre} está comiendo.")

    def dormir(self):
        print(f"{self.nombre} está durmiendo.")

# Clase Perro que hereda de Animal
class Perro(Animal):
    def __init__(self, nombre, edad, raza):
        super().__init__(nombre, edad)  # Hereda nombre y edad de la clase Animal
        self.raza = raza

    def ladrar(self):
        print(f"{self.nombre} está ladrando.")

# Clase Gato que hereda de Animal
class Gato(Animal):
    def __init__(self, nombre, edad, color_ojos):
        super().__init__(nombre, edad)  # Hereda nombre y edad de la clase Animal
        self.color_ojos = color_ojos

    def maullar(self):
        print(f"{self.nombre} está maullando.")

# Creación de objetos de las clases Perro y Gato
max = Perro(nombre="Max", edad=3, raza="Labrador")
luna = Gato(nombre="Luna", edad=2, color_ojos="Verdes")

# Uso de los atributos y métodos
print(f"Nombre: {max.nombre}, Raza: {max.raza}, Edad: {max.edad}")
max.ladrar()
max.comer()
max.dormir()
print()

print(f"Nombre: {luna.nombre}, Color de ojos: {luna.color_ojos}, Edad: {luna.edad}")
luna.maullar()
luna.comer()
luna.dormir()
print()
# Ejemplo de polimorfismo: Tratando a los objetos como instancias de la clase base Animal
animales = [max, luna]

for animal in animales:
    animal.comer()  # Ambos objetos, tanto max como luna, comparten el método comer()
