# Programa: Clasificar una edad utilizando match-case
# Descripción:
# Este programa determina la categoría de una persona
# según su edad utilizando condiciones en match-case.

# Variable que almacena la edad
edad = 20

# Evalúa la edad
match edad:
    case edad if edad < 18:
        print("Eres menor de edad.")
    case edad if edad >= 18 and edad < 65:
        print("Eres adulto.")
    case edad if edad >= 65:
        print("Eres adulto mayor.")