# Programa: Clasificar usuarios según su rol
# Descripción:
# Este programa recorre una lista de usuarios
# y muestra un mensaje según el rol de cada uno.

# Lista de usuarios
usuarios = [
    {"nombre": "Ana", "rol": "admin"},
    {"nombre": "Luis", "rol": "usuario"},
    {"nombre": "Marta", "rol": "moderador"}
]

# Recorre la lista de usuarios
for usuario in usuarios:

    # Evalúa el rol de cada usuario
    match usuario:
        case {"rol": "admin"}:
            print(f"{usuario['nombre']} tiene permisos de administrador.")

        case {"rol": "moderador"}:
            print(f"{usuario['nombre']} puede moderar contenidos.")

        case {"rol": "usuario"}:
            print(f"{usuario['nombre']} es un usuario regular.")

        case _:
            print(f"Rol de {usuario['nombre']} desconocido.")