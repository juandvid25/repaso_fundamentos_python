# Programa: Verificación de acceso condicional (OR)
# Descripción:
# Este programa evalúa si al menos una de las condiciones
# de acceso es verdadera para permitir la entrada.

# Variables
acceso_registrado = True
acceso_permitido = False

# Evalúa los permisos y muestra el mensaje
if acceso_permitido or acceso_registrado:
    print("Acceso concedido.")