# Programa: Sumar números con continue y break
# Descripción:
# Este programa recorre una lista de números,
# omite los múltiplos de 3 utilizando continue
# y detiene la suma cuando el resultado supera
# el límite establecido mediante break.

# Lista de números
numeros = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

# Límite máximo permitido para la suma
limite = 50

# Variable que almacena la suma acumulada
suma = 0

# Recorre la lista de números
for num in numeros:

    # Omite los números que son múltiplos de 3
    if num % 3 == 0:
        continue

    # Suma el número actual
    suma += num

    # Finaliza el ciclo si la suma supera el límite
    if suma > limite:
        break