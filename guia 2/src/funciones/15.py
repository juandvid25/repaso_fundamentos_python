# Programa: Suma de una cantidad variable de números
# Descripción:
# Este programa define una función que utiliza *args para
# recibir una cantidad variable de números y devuelve la
# suma total de todos ellos.

def sumar(*numeros):
    total = 0

    for numero in numeros:
        total += numero

    return total

print(sumar(1, 2))
print(sumar(1, 2, 3, 4, 5))
print(sumar())