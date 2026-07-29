# Programa: Coincidencia de patrones con listas
# Descripción:
# Este programa utiliza la estructura match-case para
# identificar la cantidad de elementos que tiene una lista.

# Lista de números
numeros = [1, 2, 3, 4]

# Evalúa la estructura de la lista
match numeros:
    case []:
        print("La lista está vacía.")

    case [uno]:
        print(f"Un solo elemento: {uno}.")

    case [uno, dos]:
        print(f"Dos elementos: {uno} y {dos}.")

    case [uno, *resto]:
        print(f"Primer elemento: {uno}, resto de la lista: {resto}.")