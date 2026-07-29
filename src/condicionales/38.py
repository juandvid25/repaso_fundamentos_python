# Programa: Verificación de acceso anidado
# Descripción:
# Este programa utiliza estructuras condicionales anidadas
# para comprobar los permisos de acceso de forma secuencial.

# Variables
acceso_registrado = True
acceso_permitido = False

# Evalúa los permisos paso a paso
if acceso_permitido:
    print("Acceso concedido.")
else:
    if acceso_registrado:
        print("Acceso concedido.")