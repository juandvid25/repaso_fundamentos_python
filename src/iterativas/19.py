# Programa: Ejemplos del uso de la instrucción continue
# Descripción:
# Este programa muestra diferentes ejemplos del uso
# de la instrucción continue para omitir determinadas
# iteraciones dentro de un ciclo.

# Ejemplo 1: Omitir números pares

# Recorre los números del 1 al 10
for numero in range(1, 11):

    # Omite los números pares
    if numero % 2 == 0:
        continue

    # Muestra únicamente los números impares
    print(f"Número impar: {numero}")


# Ejemplo 2: Filtrar temperaturas negativas

# Lista de temperaturas registradas
temperaturas = [22, -5, 28, 31, -15, 19, 26, -8]

# Recorre la lista de temperaturas
for temp in temperaturas:

    # Omite las temperaturas iguales o inferiores a cero
    if temp <= 0:
        continue

    # Muestra únicamente las temperaturas positivas
    print(f"{temp}°C")


# Ejemplo 3: Omitir divisiones por cero

# Lista de números
numeros = [1, 2, 0, 4, 0, 6, 7]

# Recorre la lista de números
for num in numeros:

    # Evita realizar una división entre cero
    if num == 0:
        print("Omitiendo división por cero")
        continue

    # Realiza y muestra la división
    print(f"10 / {num} = {10 / num}")