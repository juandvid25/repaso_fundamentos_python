# Programa: Recorrer un diccionario de diferentes formas
# Descripción:
# Este programa muestra la información de un diccionario
# recorriendo sus claves, sus pares clave-valor
# y únicamente sus valores.

# Diccionario con información de un usuario
usuario = {"nombre": "Laura", "edad": 28, "ciudad": "Madrid"}

# Recorre el diccionario mostrando cada clave y su valor
for clave in usuario:
    print(f"Clave: {clave}, Valor: {usuario[clave]}")

# Recorre el diccionario mostrando las claves y los valores con items()
for clave, valor in usuario.items():
    print(f"{clave}: {valor}")

# Recorre el diccionario mostrando únicamente los valores
for valor in usuario.values():
    print(valor)