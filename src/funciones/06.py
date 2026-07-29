# Programa: Cálculo de descuento con parámetro opcional
# Descripción:
# Este programa define una función que calcula el precio final
# de un producto aplicando un porcentaje de descuento. Si no
# se especifica el porcentaje, utiliza un 10% por defecto.

def calcular_descuento(precio, porcentaje=10):
    descuento = precio * (porcentaje / 100)
    precio_final = precio - descuento
    return precio_final

precio_con_descuento = calcular_descuento(100)

print(f"Precio con descuento: {precio_con_descuento}")