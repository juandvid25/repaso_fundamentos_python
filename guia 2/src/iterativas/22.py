# Programa: Validación de contraseña y procesamiento de transacciones
# Descripción:
# Este programa valida que una contraseña cumpla
# con requisitos básicos de seguridad y calcula
# el total de las transacciones completadas con
# montos mayores que cero.

# Función que valida una contraseña
def validar_contraseña(contraseña):

    # Verifica que la contraseña tenga al menos 8 caracteres
    if len(contraseña) < 8:
        return False

    # Variables para verificar los requisitos de la contraseña
    tiene_mayuscula = tiene_minuscula = tiene_numero = False

    # Recorre cada carácter de la contraseña
    for caracter in contraseña:

        # Verifica si el carácter es una letra mayúscula
        if caracter.isupper():
            tiene_mayuscula = True
            continue

        # Verifica si el carácter es una letra minúscula
        if caracter.islower():
            tiene_minuscula = True
            continue

        # Verifica si el carácter es un número
        if caracter.isdigit():
            tiene_numero = True

    # Devuelve True si cumple todos los requisitos
    return tiene_mayuscula and tiene_minuscula and tiene_numero


# Lista de transacciones
transacciones = [
    {"id": 1, "monto": 1200, "estado": "completada"},
    {"id": 2, "monto": -50, "estado": "error"},
    {"id": 3, "monto": 800, "estado": "pendiente"},
    {"id": 4, "monto": 1500, "estado": "completada"},
    {"id": 5, "monto": 0, "estado": "cancelada"}
]

# Variable para acumular el total de las transacciones válidas
total = 0

# Recorre la lista de transacciones
for t in transacciones:

    # Omite las transacciones no completadas o con monto menor o igual a cero
    if t["estado"] != "completada" or t["monto"] <= 0:
        continue

    # Suma el monto de las transacciones válidas
    total += t["monto"]