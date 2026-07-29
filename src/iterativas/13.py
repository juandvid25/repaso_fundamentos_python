# Programa: Confirmar si el usuario desea continuar
# Descripción:
# Este programa solicita al usuario que indique
# si desea continuar o finalizar la ejecución.
# El ciclo se repite hasta que el usuario
# decida salir.

# Repite el ciclo de forma indefinida
while True:

    # Solicita una respuesta al usuario y la convierte a minúsculas
    respuesta = input("¿Quieres continuar? (s/n): ").lower()

    # Finaliza el programa si la respuesta es "n"
    if respuesta == "n":
        print("Programa finalizado.")
        break

    # Continúa la ejecución si la respuesta es "s"
    if respuesta == "s":
        print("Continuando...")

    # Muestra un mensaje si la respuesta no es válida
    else:
        print("Respuesta no válida. Introduce 's' o 'n'.")