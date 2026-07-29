# Programa: División segura con operador ternario
# Descripción:
# Este programa realiza una división utilizando el operador
# ternario para evitar la división por cero de forma directa.

# Variables
dividendo = 10
divisor = 0

# Evalúa y calcula la división
resultado = dividendo / divisor if divisor != 0 else "División por cero no permitida"

# Muestra el resultado
print(resultado)