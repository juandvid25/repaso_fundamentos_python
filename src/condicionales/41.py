# Programa: Verificación total con all()
# Descripción:
# Este programa utiliza la función all() para verificar
# si todas las condiciones de una lista son verdaderas.

# Variable
condiciones = [True, True, False, True]

# Evalúa si todas las condiciones se cumplen
if all(condiciones):
    print("Todas las condiciones son verdaderas.")
else:
    print("Al menos una condición es falsa.")