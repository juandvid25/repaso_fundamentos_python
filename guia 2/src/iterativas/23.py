# Programa: Uso de la instrucción pass
# Descripción:
# Este programa recorre los números del 1 al 9.
# La instrucción pass se utiliza como un marcador
# de posición para no realizar ninguna acción
# cuando el número es par.

# Recorre los números del 1 al 9
for numero in range(1, 10):

    # Verifica si el número es par
    if numero % 2 == 0:

        # No realiza ninguna acción
        pass

    # Si el número es impar, lo muestra en pantalla
    else:
        print(f"Procesando número impar: {numero}")