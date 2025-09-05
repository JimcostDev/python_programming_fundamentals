import bcrypt

# --- SIMULACIÓN DEL REGISTRO DE USUARIO ---
# 1. Se define la contraseña del usuario.
password = 'mi_super_contraseña_secreta_123'.encode('utf-8')

# 2. Se genera una sal (salt) aleatoria.
salt = bcrypt.gensalt()

# 3. Se hashea la contraseña con la sal.
# El hash resultante ya contiene la sal y otros metadatos.
hashed_password = bcrypt.hashpw(password, salt)

# Imaginemos que `hashed_password` es lo que se guarda en la base de datos.
print(f"Contraseña en texto plano: {password.decode()}")
print(f"Hash almacenado en la DB: {hashed_password.decode()}")
print("\n--- SIMULACIÓN DEL LOGIN ---")

# --- SIMULACIÓN DEL LOGIN ---
# 1. El usuario introduce la contraseña para iniciar sesión.
login_password = 'mi_super_contraseña_secreta_123'.encode('utf-8')

# 2. Se recupera el hash almacenado de la base de datos (en este caso, `hashed_password`).
# bcrypt extrae automáticamente la sal del propio hash para la verificación.
# No es necesario almacenar la sal por separado si se usa bcrypt.

# 3. Se utiliza bcrypt.checkpw() para comparar la contraseña ingresada con el hash guardado.
# Compara el nuevo hash que acaba de generar con el hash que está guardado en la base de datos.
# Si los dos hashes son idénticos, la función devuelve True, lo que significa que la contraseña es correcta. Si no, devuelve False.
if bcrypt.checkpw(login_password, hashed_password):
    print("¡Contraseña correcta! Acceso concedido.")
else:
    print("Contraseña incorrecta. Acceso denegado.")

print("\n--- EJEMPLO CON CONTRASEÑA INCORRECTA ---")
# Probamos con una contraseña incorrecta.
wrong_password = 'contraseña_incorrecta'.encode('utf-8')

if bcrypt.checkpw(wrong_password, hashed_password):
    print("¡Contraseña correcta! Acceso concedido.")
else:
    print("Contraseña incorrecta. Acceso denegado.")