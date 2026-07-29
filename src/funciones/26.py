# Programa: Creación de listas y diccionarios
# Descripción:
# Este programa crea una lista de números pares y un
# diccionario con el cuadrado de cada número.

# Función que genera una lista de números pares
def crear_lista_pares(maximo):
    return [num for num in range(2, maximo + 1, 2)]

# Función que crea un diccionario con los cuadrados
def crear_diccionario_cuadrados(numeros):
    return {num: num ** 2 for num in numeros}

# Genera la lista de números pares
pares = crear_lista_pares(10)

# Muestra la lista de números pares
print(pares)

# Genera el diccionario de cuadrados
cuadrados = crear_diccionario_cuadrados([1, 2, 3, 4])

# Muestra el diccionario
print(cuadrados)