# Programa: Clasificar una persona según su edad
# Descripción:
# Este programa determina si una persona es menor de edad,
# adulta o mayor de 65 años.

# Variable que almacena la edad
edad = 45

# Evalúa la edad
if edad < 18:
    print("Eres menor de edad.")
elif 18 <= edad < 65:
    print("Eres adulto.")
else:
    print("Eres mayor de 65 años.")