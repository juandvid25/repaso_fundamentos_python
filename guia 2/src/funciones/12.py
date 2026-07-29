# Programa: Creación de un usuario con argumentos nombrados
# Descripción:
# Este programa define una función que crea un usuario
# utilizando argumentos nombrados y devuelve la información
# en forma de diccionario.

def crear_usuario(nombre, apellido, edad, email, activo=True):
    return {
        "nombre_completo": f"{nombre} {apellido}",
        "edad": edad,
        "email": email,
        "activo": activo
    }

usuario = crear_usuario(
    nombre="Juan",
    apellido="Pérez",
    edad=28,
    email="juan@ejemplo.com",
    activo=False
)