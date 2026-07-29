# Programa: Determinación de paridad en listas
# Descripción:
# Este programa aplica comprensión de listas junto con un
# operador ternario para determinar si cada número es par o impar.

# Variable
numeros = [1, 2, 3, 4, 5]

# Determina la paridad de cada elemento
paridad = ["par" if n % 2 == 0 else "impar" for n in numeros]

# Muestra el resultado
print(paridad)