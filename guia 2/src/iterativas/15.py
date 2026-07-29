# Programa: Calcular la raíz cuadrada de un número
# Descripción:
# Este programa define una función que calcula
# la raíz cuadrada de un número utilizando
# aproximaciones sucesivas hasta alcanzar
# una precisión determinada.

# Función que calcula la raíz cuadrada de un número
def calcular_raiz_cuadrada(numero, precision=0.0001):

    # Establece una aproximación inicial
    aproximacion = numero / 2

    # Repite el cálculo hasta obtener la precisión deseada
    while abs(aproximacion ** 2 - numero) > precision:
        aproximacion = (aproximacion + numero / aproximacion) / 2

    # Devuelve la aproximación de la raíz cuadrada
    return aproximacion

# Llama a la función y muestra el resultado
print(calcular_raiz_cuadrada(25))