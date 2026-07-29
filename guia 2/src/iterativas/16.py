# Programa: Imprimir un triángulo con asteriscos
# Descripción:
# Este programa define una función que imprime
# un triángulo formado por asteriscos según
# la altura indicada por el usuario.

# Función que imprime un triángulo de asteriscos
def imprimir_triangulo(altura):

    # Inicializa el contador de filas
    fila = 1

    # Repite el ciclo hasta alcanzar la altura indicada
    while fila <= altura:

        # Imprime una fila con la cantidad de asteriscos correspondiente
        print("*" * fila)

        # Incrementa el contador de filas
        fila += 1

# Llama a la función con una altura de 5
imprimir_triangulo(5)