# Programa: Uso de rangos numéricos con range()
# Descripción:
# Este programa demuestra el uso de la función range() para generar 
# secuencias de números con distintos inicios, fines, pasos y orden inverso.

# Rango simple (del 0 al 4)
for i in range(5):
    print(i)

# Rango inicio y fin (3 al 7)
for i in range(3, 8):
    print(i, end=" ")
print()

# Rango con paso (pares del 2 al 10)
for i in range(2, 11, 2):
    print(i, end=" ")
print()

# Cuenta regresiva (del 10 al 1)
for i in range(10, 0, -1):
    print(i, end=" ")
