# Programa: Control de saldo disponible
# Descripción:
# Este programa permite registrar gastos mientras
# exista saldo disponible. También permite salir
# del programa cuando el usuario ingresa 0 y evita
# realizar gastos superiores al saldo.

# Saldo inicial disponible
saldo = 1000

# Repite el ciclo mientras exista saldo
while saldo > 0:

    # Muestra el saldo actual
    print(f"Saldo actual: {saldo} €")

    # Solicita al usuario la cantidad que desea gastar
    gasto = float(input("Introduce la cantidad a gastar (0 para salir): "))

    # Finaliza el programa si el usuario ingresa 0
    if gasto == 0:
        break

    # Verifica si el gasto supera el saldo disponible
    if gasto > saldo:
        print("No tienes suficiente saldo.")
        continue

    # Descuenta el gasto del saldo
    saldo -= gasto

# Muestra el saldo restante
print(f"Saldo final: {saldo} €")