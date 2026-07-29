# Programa: Documentación de una función con docstring
# Descripción:
# Este programa define una función que calcula el promedio
# de dos números. Además, muestra la documentación de la
# función utilizando el atributo __doc__ y la función help().

# Función que calcula el promedio de dos números
def calcular_promedio(a, b):
    """
    Calcula el promedio de dos números.

    Parámetros:
        a (float): Primer número.
        b (float): Segundo número.

    Retorna:
        float: El promedio de los dos números.
    """

    # Devuelve el promedio de los dos números
    return (a + b) / 2

# Muestra únicamente el contenido del docstring
print(calcular_promedio.__doc__)

# Muestra la ayuda completa de la función
help(calcular_promedio)