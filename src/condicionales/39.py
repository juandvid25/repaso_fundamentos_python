# Programa: Verificación de acceso con lógica agrupada
# Descripción:
# Este programa combina operadores lógicos OR y AND
# mediante paréntesis para determinar el acceso.

# Variables
acceso_registrado = True
acceso_permitido = False

# Evalúa las condiciones agrupadas
if acceso_permitido or (acceso_registrado and True):
    print("Acceso concedido.")