# Programa: Contador de palabras
# Descripción:
# Este programa define una función que cuenta la cantidad
# de palabras contenidas en un texto.

# Función que cuenta las palabras de un texto
def contar_palabras(texto):
    """
    Cuenta el número de palabras en un texto.
    """

    # Devuelve la cantidad de palabras del texto
    return len(texto.split())