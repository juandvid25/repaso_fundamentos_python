# Programa: Uso de argumentos nombrados variables
# Descripción:
# Este programa define una función que utiliza **kwargs
# para recibir una cantidad variable de argumentos
# nombrados y mostrar su información en pantalla.

def mostrar_informacion(**datos):
    for clave, valor in datos.items():
        print(f"{clave}: {valor}")

mostrar_informacion(
    nombre="Python",
    creador="Guido van Rossum",
    año=1991
)