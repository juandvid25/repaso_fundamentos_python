# Programa: Mostrar la tabla de multiplicar del 1 al 3
# Descripción:
# Este programa utiliza ciclos for anidados para
# mostrar las multiplicaciones de los números
# del 1 al 3 en formato de tabla.

# Recorre los números del 1 al 3
for i in range(1, 4):

    # Recorre los números del 1 al 3 para realizar las multiplicaciones
    for j in range(1, 4):
        print(f"{i} × {j} = {i * j}", end="\t")

    # Salta a la siguiente línea al terminar cada fila de la tabla
    print()