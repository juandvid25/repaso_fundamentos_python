# Programa: Cálculo del precio con IVA
# Descripción:
# Este programa calcula el precio final de un producto
# aplicando un porcentaje de IVA.

# Función que calcula el precio con IVA
def calcular_precio_con_iva(precio_base, tasa_iva=0.21):
    return precio_base * (1 + tasa_iva)

# Calcula el precio final
precio_final = calcular_precio_con_iva(100)

# Muestra el resultado
print(precio_final)