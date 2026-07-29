# Programa: Uso de paréntesis en expresiones lógicas
# Descripción:
# Este programa demuestra cómo los paréntesis modifican
# el orden de evaluación de una expresión lógica.

# Variables
a = True
b = False
c = not b

# Evalúa la expresión lógica
resultado = (a or b) and c

# Muestra el resultado
print(resultado)