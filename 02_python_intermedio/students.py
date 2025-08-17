# Supongamos que queremos gestionar una lista de estudiantes con su edad y calificación.
# Usaremos listas + diccionarios:

# Lista de estudiantes (cada uno es un diccionario)
estudiantes = [
    {"nombre": "Ana", "edad": 20, "nota": 8.5},
    {"nombre": "Luis", "edad": 22, "nota": 9.0},
    {"nombre": "Marta", "edad": 21, "nota": 7.3}
]

# Mostrar todos los estudiantes
for est in estudiantes:
    print(est["nombre"], "-> Edad:", est["edad"], "Nota:", est["nota"])

# Buscar el estudiante con mejor nota
mejor = max(estudiantes, key=lambda x: x["nota"])
print("\nMejor estudiante:", mejor["nombre"], "con nota", mejor["nota"])

# Calcular promedio de notas
promedio = sum(est["nota"] for est in estudiantes) / len(estudiantes)
print("Promedio de notas:", promedio)

