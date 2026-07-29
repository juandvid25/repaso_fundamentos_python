# Programa: Simulación de un retiro bancario
# Descripción:
# Este programa verifica si el saldo disponible es suficiente
# para realizar un retiro.

# Variables
saldo = 300
retiro = 500

# Comprueba si hay fondos suficientes
if saldo >= retiro:
    saldo -= retiro
    print("Retiro exitoso.")
    print(f"Nuevo saldo: {saldo}")
else:
    print("Fondos insuficientes.")
    print(f"Saldo actual: {saldo}")