# Programa: Cálculo de una expresión matemática
# Autor: Juan David
# Descripción:
# Este programa convierte un número entero a decimal (float),
# evalúa una expresión matemática y muestra el resultado.

# Se declara la variable x con un valor entero.
x = 3

# Se convierte el valor de x al tipo de dato decimal (float).
x = float(x)

# Se calcula el valor de la expresión:
# y = 3x³ - 2x² + 3x - 1
y = 3 * x**3 - 2 * x**2 + 3 * x - 1

# Se muestra el resultado de la operación.
print("y =", y)