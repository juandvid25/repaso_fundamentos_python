# Programa: Cálculo de pago con parámetros opcionales
# Descripción:
# Este programa define una función que calcula el pago de
# un trabajador utilizando parámetros con valores
# predeterminados y diferentes formas de llamar la función.

def calcular_pago(horas, tarifa=15, moneda="EUR"):
    total = horas * tarifa
    return f"{total} {moneda}"

pago1 = calcular_pago(40)
pago2 = calcular_pago(35, 20)
pago3 = calcular_pago(30, moneda="USD")
pago4 = calcular_pago(horas=25, tarifa=18, moneda="GBP")

print(pago1)
print(pago2)
print(pago3)
print(pago4)