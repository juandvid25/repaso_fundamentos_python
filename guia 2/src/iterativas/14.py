# Programa: Calcular el factorial de un número
# Descripción:
# Este programa define una función que calcula
# el factorial de un número utilizando un ciclo
# while y muestra el resultado obtenido.

# Función que calcula el factorial de un número
def calcular_factorial(n):

    # Inicializa la variable que almacenará el resultado
    resultado = 1

    # Multiplica los números desde n hasta 1
    while n > 0:
        resultado *= n
        n -= 1

    # Devuelve el factorial calculado
    return resultado

# Llama a la función y muestra el resultado
print(calcular_factorial(5))