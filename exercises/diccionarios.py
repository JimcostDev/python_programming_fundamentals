
# Crear un diccionario que asocia nombres de equipos con sus colores
equipos = {
    "Deportivo Cali": "Verde 💚",
    "Liverpool": "Rojo ❤️",
    "Real Madrid": "Blanco 🤍",
}

# Acceder a un valor en el diccionario
print("Color de Deportivo Cali:", equipos["Deportivo Cali"])

# Agregar un nuevo equipo al diccionario
equipos["Barcelona"] = "Grana y Azul 💙❤️"

# Verificar si una clave existe en el diccionario
if "Boca Juniors" in equipos:
    print("Color de Boca Juniors:", equipos["Boca Juniors"])
else:
    print("Boca Juniors no está en el diccionario.")

# Recorrer el diccionario
print("Equipos y sus colores:")
for equipo, color in equipos.items():
    print(f"- {equipo}: {color}")

# Eliminar un equipo del diccionario
equipos.pop("Real Madrid", None)

# Imprimir el diccionario actualizado
print("Diccionario actualizado:", equipos)
