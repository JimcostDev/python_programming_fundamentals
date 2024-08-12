from persona import Persona

def main():
    # Crear un objeto de la clase Persona
    persona1 = Persona("Ronaldo", 25, 66, 1.84)

    # Utilizar los métodos del objeto
    persona1.saludar()
    print(persona1.get_nombre())

    # Modificar los atributos usando los setters
    persona1.set_nombre("Cristiano")
    print(persona1.get_nombre())

if __name__ == "__main__":
    main()
