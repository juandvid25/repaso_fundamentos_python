# Programa: Cálculo del precio con descuento
# Descripción:
# Este programa define una función que calcula el precio final
# de un producto después de aplicar un porcentaje de descuento.
# Además, incluye un docstring que describe la función.

# Función que calcula el precio con descuento
def calcular_descuento(precio, porcentaje):
    """
    Calcula el precio con descuento.
    """

    # Devuelve el precio final aplicando el porcentaje de descuento
    return precio - (precio * porcentaje / 100)