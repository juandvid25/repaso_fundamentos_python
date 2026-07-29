# Programa: Cálculo del área de un rectángulo
# Descripción:
# Este programa define una función que recibe la base y la
# altura de un rectángulo, calcula su área y devuelve el
# resultado para posteriormente imprimirlo.

def calcular_area_rectangulo(base, altura):
    area = base * altura
    return area

# Uso de la función
resultado = calcular_area_rectangulo(5, 3)
print(f"El área del rectángulo es: {resultado}")