# Programa: Clasificación por edad y estado civil
# Descripción:
# Este programa determina si una persona es mayor
# de edad y muestra su estado civil.

# Variables
edad = 30
estado_civil = "soltero"

# Comprueba la edad y el estado civil
if edad >= 18:
    if estado_civil == "casado":
        print("Eres un adulto casado.")
    else:
        print("Eres un adulto soltero.")
else:
    print("Eres menor de edad.")