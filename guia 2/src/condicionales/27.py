# Programa: Validación de acceso al sistema
# Descripción:
# Este programa verifica si el usuario existe y si
# la contraseña ingresada es correcta.

# Variables
usuario = "admin"
contrasena = "1234"

# Comprueba el usuario y la contraseña
if usuario == "admin":
    if contrasena == "1234":
        print("Acceso concedido.")
    else:
        print("Contraseña incorrecta.")
else:
    print("Usuario no reconocido.")