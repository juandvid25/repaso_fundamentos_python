# Programa: Cálculo del precio final con impuesto
# Descripción:
# Este programa define una función que calcula el precio final
# de un producto aplicando un porcentaje de impuesto sobre el
# precio base y muestra el resultado obtenido.

def calcular_precio_final(precio_base, impuesto):
    return precio_base + (precio_base * impuesto)

total = calcular_precio_final(100, 0.21)

print(f"Precio final: {total}")