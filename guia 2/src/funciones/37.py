# Programa: Filtrado de números pares
# Descripción:
# Este programa define una función que recibe una lista
# de números y devuelve únicamente los valores pares.

# Función que filtra los números pares de una lista
def filtrar_pares(lista):
    """
    Filtra los números pares de una lista.
    """

    # Devuelve una lista con los números pares
    return [num for num in lista if num % 2 == 0]