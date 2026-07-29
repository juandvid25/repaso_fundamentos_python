# Programa: Evaluación de división con atajo lógico
# Descripción:
# Este programa valida que el divisor no sea cero
# antes de realizar la división para evitar un error.

# Variables
dividendo = 10
divisor = 0

# Evalúa la condición y muestra el mensaje
if divisor != 0 and dividendo / divisor > 1:
    print("El resultado de la división es mayor que 1.")
else:
    print("No es posible dividir entre cero.")