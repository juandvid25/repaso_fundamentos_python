# Programa: Buscar un elemento y finalizar por comando del usuario
# Descripción:
# Este programa incluye una función para buscar
# un elemento en una lista y un ciclo que permite
# al usuario escribir mensajes hasta que decida
# finalizar el programa.

# Función que busca un elemento dentro de una lista
def buscar_elemento(lista, objetivo):

    # Recorre la lista junto con sus índices
    for indice, elemento in enumerate(lista):

        # Verifica si el elemento coincide con el objetivo
        if elemento == objetivo:
            return indice

    # Devuelve -1 si el elemento no se encuentra
    return -1


# Repite el ciclo hasta que el usuario decida salir
while True:

    # Solicita una entrada al usuario
    entrada = input("Escribe algo (o 'salir' para terminar): ")

    # Finaliza el ciclo si el usuario escribe "salir"
    if entrada.lower() == "salir":
        break

    # Muestra el texto ingresado por el usuario
    print(f"Has escrito: {entrada}")