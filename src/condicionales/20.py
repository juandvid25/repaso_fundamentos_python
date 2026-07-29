# Programa: Validación para obtener la licencia
# Descripción:
# Este programa verifica si una persona puede obtener
# la licencia de conducir según su edad y permiso parental.

# Variables
edad = 17
permiso_parental = True

# Comprueba si cumple las condiciones
if (edad >= 18) or (edad >= 16 and permiso_parental):
    print("Puedes obtener la licencia de conducir.")
else:
    print("No cumples los requisitos para la licencia.")