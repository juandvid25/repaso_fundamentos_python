# Programa: Validación de mayoría de edad
# Descripción:
# Este programa verifica si una persona es mayor de edad
# y muestra si tiene acceso permitido o denegado.

# Función que verifica si una persona es mayor de edad
def es_mayor_de_edad(edad):
    return edad >= 18

# Función que valida un correo electrónico
def es_correo_valido(email):
    return "@" in email and "." in email

# Edad del usuario
usuario_edad = 16

# Verifica si el usuario puede acceder
if es_mayor_de_edad(usuario_edad):
    print("Acceso permitido")
else:
    print("Acceso denegado")