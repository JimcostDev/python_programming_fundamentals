# variables
nombre = 'Ronaldo'
apellido = 'Jimenez Acosta'
telefono = '1326753768'

# concatenar string
nombre_completo = nombre + " " + apellido
print(nombre_completo)

# diferentes uso de las comillas
presentacion = """
                I'm from Colombia and 
                I'm software developer, 
                I have 23 years old.
                """
print(presentacion)


cita = 'El dijo: "Hola"'
print(cita)


# format
informacion = "Soy: " + nombre + " " + apellido + ", " + " mi numero de telefono es: " + telefono
print(informacion)

informacion = "Soy: {} {},  mi numero de telefono es:  {}".format(nombre,apellido,telefono)
print(informacion)

informacion = f"Soy: {nombre} {apellido},  mi numero de telefono es:  {telefono}"
print(informacion)