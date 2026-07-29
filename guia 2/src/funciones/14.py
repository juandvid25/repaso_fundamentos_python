# Programa: Validación de datos en una función
# Descripción:
# Este programa define una función que calcula el precio
# final de un producto aplicando un descuento. Además,
# valida que el precio y el porcentaje sean valores
# correctos y maneja los errores mediante excepciones.

def calcular_descuento(precio, porcentaje):

    if not isinstance(precio, (int, float)) or precio < 0:
        raise ValueError("El precio debe ser un número positivo")

    if not isinstance(porcentaje, (int, float)) or not (0 <= porcentaje <= 100):
        raise ValueError("El porcentaje debe ser un número entre 0 y 100")

    descuento = precio * (porcentaje / 100)
    return precio - descuento

try:
    precio_final = calcular_descuento(100, 15)
    print(f"Precio con descuento: {precio_final}")

    precio_erroneo = calcular_descuento(-50, 10)

except ValueError as e:
    print(f"Error: {e}")