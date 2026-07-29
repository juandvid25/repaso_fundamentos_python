# Programa: Recorrer una lista mostrando índices y nombres
# Descripción:
# Este programa muestra los elementos de una lista
# utilizando dos métodos diferentes: range(len())
# y enumerate(), indicando la posición de cada nombre.

# Lista de nombres
nombres = ["Ana", "Carlos", "Elena"]

# Recorre la lista utilizando los índices
for i in range(len(nombres)):
    print(f"Posición {i}: {nombres[i]}")

# Recorre la lista utilizando enumerate()
for indice, nombre in enumerate(nombres):
    print(f"Posición {indice}: {nombre}")