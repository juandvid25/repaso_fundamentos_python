# Programa: Uso de argumentos posicionales y nombrados
# Descripción:
# Este programa define una función para dividir dos números
# y demuestra cómo llamarla utilizando argumentos
# posicionales y argumentos nombrados.

def dividir(dividendo, divisor):
    return dividendo / divisor

resultado1 = dividir(10, 2)

resultado2 = dividir(divisor=2, dividendo=10)