# Programa: Salir de ciclos anidados con break
# Descripción:
# Este programa utiliza una variable de control
# para salir de dos ciclos anidados cuando se
# encuentra una condición determinada.

# Variable que indica si se encontró la condición
encontrado = False

# Recorre los valores de i del 0 al 4
for i in range(5):

    # Recorre los valores de j del 0 al 4
    for j in range(5):

        # Verifica si el producto de i y j es mayor que 10
        if i * j > 10:

            # Indica que la condición fue encontrada
            encontrado = True

            # Sale del ciclo interno
            break

    # Si la condición fue encontrada, sale del ciclo externo
    if encontrado:
        break