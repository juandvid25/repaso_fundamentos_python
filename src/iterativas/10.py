# Programa: Validar la entrada de un número
# Descripción:
# Este programa solicita al usuario que ingrese
# un número y continúa pidiéndolo hasta que
# la entrada sea válida.

# Variable para almacenar la entrada del usuario
entrada = ""

# Repite el ciclo mientras la entrada no sea un número
while not entrada.isdigit():
    entrada = input("Introduce un número: ")

# Muestra el número ingresado por el usuario
print(f"Has introducido el número: {entrada}")