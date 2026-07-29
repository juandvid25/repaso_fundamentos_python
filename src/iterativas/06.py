# Programa: Crear listas mediante comprensión de listas
# Descripción:
# Este programa utiliza comprensión de listas para
# generar una lista de cuadrados y otra con
# únicamente los números pares.

# Genera una lista con los cuadrados de los números del 1 al 5
cuadrados = [x ** 2 for x in range(1, 6)]

# Genera una lista con los números pares del 0 al 9
pares = [x for x in range(10) if x % 2 == 0]