# Programa: División segura
# Descripción:
# Este programa realiza una división verificando que
# el divisor no sea cero para evitar errores.

# Función que realiza una división segura
def dividir_seguro(a, b):

    # Verifica si el divisor es cero
    if b == 0:
        print("Error: División por cero")
        return None

    # Realiza la división
    resultado = a / b

    # Devuelve el resultado
    return resultado

# División válida
print(dividir_seguro(10, 2))

# División con divisor igual a cero
print(dividir_seguro(10, 0))