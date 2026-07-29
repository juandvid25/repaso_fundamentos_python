# Programa: Conversión de temperaturas
# Descripción:
# Este programa convierte temperaturas entre grados
# Celsius, Fahrenheit y Kelvin, validando que las
# unidades ingresadas sean correctas.

# Función que convierte temperaturas entre diferentes unidades
def convertir_temperatura(valor, origen, destino):

    # Conjunto de unidades válidas
    unidades_validas = {"C", "F", "K"}

    # Verifica que las unidades sean válidas
    if origen not in unidades_validas or destino not in unidades_validas:
        return None

    # Si las unidades son iguales, devuelve el mismo valor
    if origen == destino:
        return valor

    # Convierte la temperatura a grados Celsius
    if origen == "F":
        celsius = (valor - 32) * 5 / 9
    elif origen == "K":
        celsius = valor - 273.15
    else:
        celsius = valor

    # Convierte desde Celsius a la unidad de destino
    if destino == "F":
        return celsius * 9 / 5 + 32
    elif destino == "K":
        return celsius + 273.15
    else:
        return celsius

# Ejemplos de conversión
print(convertir_temperatura(25, "C", "F"))
print(convertir_temperatura(98.6, "F", "C"))
print(convertir_temperatura(0, "C", "K"))
print(convertir_temperatura(20, "X", "Y"))