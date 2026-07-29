# Programa: Filtrado de números positivos
# Descripción:
# Este programa define una función que recibe una lista de números.
# Si el dato recibido no es una lista, devuelve una lista vacía.
# En caso contrario, devuelve únicamente los números positivos.

# Función que filtra los números positivos de una lista
def filtrar_positivos(numeros):

    # Verifica que el dato recibido sea una lista
    if not isinstance(numeros, list):
        return []

    # Devuelve una nueva lista con los números mayores que cero
    return [num for num in numeros if num > 0]