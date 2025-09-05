from persona import Futbolista, Doctor

# Creación de objetos de las clases Futbolista y Doctor y uso de los métodos
ronaldo = Futbolista("Cristiano Ronaldo", 38, 85, 1.87, "Delantero", "Portugal")
ronaldo.saludar()
ronaldo.jugar()
ronaldo.dormir() # El método dormir de la clase Futbolista sobreescribe el método dormir de la clase Persona
print()

house = Doctor("Gregory House", 60, 75, 1.85, "Diagnóstico", "Princeton-Plainsboro")
house.saludar()     
house.tratar_paciente()
house.dormir()
print()

# Ejemplo de polimorfismo: Tratando a los objetos como instancias de la clase base Persona
personas = [ronaldo, house]
for persona in personas:
    persona.dormir()  # Ambos objetos, tanto ronaldo como house, comparten el método dormir de la clase Persona
    
# llamar a __str__ de la clase Persona
print()
print(ronaldo)  
print(house)