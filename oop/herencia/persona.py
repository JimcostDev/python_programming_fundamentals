# Definición de la clase Persona, base
class Persona:
    def __init__(self, nombre="", edad=0, peso=0.0, estatura=0.0):
        self.nombre = nombre
        self.edad = edad
        self.peso = peso
        self.estatura = estatura
    
    # __str__ es un método especial que se llama cuando se imprime el objeto
    def __str__(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Peso: {self.peso}, Estatura: {self.estatura}"
    
    def saludar(self):
        print(f"Hola, mi nombre es: {self.nombre}")
    
    def dormir(self):
        print(f"{self.nombre} está durmiendo.")
        
# Definición de la clase Futbolista, que hereda de Persona
class Futbolista(Persona):
    def __init__(self, nombre, edad, peso, estatura, posicion, equipo):
        super().__init__(nombre, edad, peso, estatura)
        self.posicion = posicion
        self.equipo = equipo
    
    def jugar(self):
        print(f"{self.nombre} está jugando en la posición de {self.posicion} en el equipo {self.equipo}")
    
    def dormir(self):
        print(f"{self.nombre} está durmiendo en el autobús del equipo.")
        
# Definición de la clase Doctor, que hereda de Persona
class Doctor(Persona):
    def __init__(self, nombre, edad, peso, estatura, especialidad, hospital):
        super().__init__(nombre, edad, peso, estatura)
        self.especialidad = especialidad
        self.hospital = hospital
    
    def tratar_paciente(self):
        print(f"{self.nombre} está tratando a un paciente en el hospital {self.hospital}")
    
    def dormir(self):
        print(f"{self.nombre} está durmiendo en su casa.")
        

