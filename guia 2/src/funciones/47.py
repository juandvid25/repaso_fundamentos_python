# Programa: Cálculo del precio final de un producto
# Descripción:
# Este programa calcula el precio final de un producto
# aplicando un descuento y un impuesto, validando que
# los valores ingresados sean correctos.

# Función que calcula el precio final
def calcular_precio_final(precio_base, descuento=0, impuesto=0.21):

    # Verifica que los valores no sean negativos
    if precio_base < 0 or descuento < 0 or impuesto < 0:
        raise ValueError("Los valores no pueden ser negativos")

    # Calcula el precio después del descuento
    precio_con_descuento = precio_base * (1 - descuento / 100)

    # Calcula el precio final con el impuesto
    precio_final = precio_con_descuento * (1 + impuesto)

    # Devuelve el precio final
    return precio_final