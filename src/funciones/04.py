# Programa: Conversión de Celsius a Fahrenheit
# Descripción:
# Este programa define una función que convierte una temperatura
# expresada en grados Celsius a grados Fahrenheit utilizando
# la fórmula de conversión correspondiente.

def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Uso de la función
temperatura_fahrenheit = celsius_a_fahrenheit(25)
print(f"25°C equivalen a {temperatura_fahrenheit}°F")