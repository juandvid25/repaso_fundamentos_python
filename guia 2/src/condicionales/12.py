# Programa: Identificar una fruta
# Descripción:
# Este programa solicita una fruta al usuario
# y utiliza la estructura match-case para identificarla.

# Solicita una fruta al usuario
fruta = input("Introduzca una fruta: ")

# Evalúa la fruta ingresada
match fruta:
    case "manzana":
        print("La fruta es una manzana.")
    case "naranja":
        print("La fruta es una naranja.")
    case "plátano":
        print("La fruta es un plátano.")
    case _:
        print("Fruta desconocida.")