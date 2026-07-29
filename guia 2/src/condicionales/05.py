# Programa: Validación de contraseña
# Descripción:
# Este programa solicita una contraseña al usuario y verifica
# si coincide con la contraseña almacenada.

# Solicita la contraseña al usuario
contrasena = input("Introduce la contraseña: ")

# Verifica si la contraseña es correcta
if contrasena == "secreta123":
    print("Acceso concedido.")
else:
    print("Contraseña incorrecta. Acceso denegado.")