# Programa: Ejemplos prácticos del uso de ciclos for
# Descripción:
# Este programa presenta tres ejemplos del uso de ciclos for:
# calcular la suma de los primeros n números,
# identificar números primos y analizar
# un conjunto de temperaturas.

# Ejemplo 1: Suma de los primeros n números

# Cantidad de números a sumar
n = 10

# Variable para almacenar la suma
suma = 0

# Recorre los números del 1 hasta n y acumula su suma
for i in range(1, n + 1):
    suma += i

# Muestra el resultado de la suma
print(f"La suma de los primeros {n} números es: {suma}")


# Ejemplo 2: Números primos en un rango

# Función que verifica si un número es primo
def es_primo(num):
    if num < 2:
        return False

    # Comprueba si el número tiene divisores
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False

    return True

# Crea una lista con los números primos entre 2 y 19
primos = [num for num in range(2, 20) if es_primo(num)]


# Ejemplo 3: Procesamiento de datos (temperaturas)

# Lista de temperaturas registradas
temperaturas = [22, 19, 24, 25, 21, 23, 20]

# Lista con los días de la semana
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

# Obtiene la temperatura más alta
max_temp = max(temperaturas)

# Encuentra la posición de la temperatura máxima
indice_max = temperaturas.index(max_temp)

# Muestra el día con la mayor temperatura
print(f"El día más caluroso fue {dias[indice_max]} con {max_temp}°C")

# Calcula la temperatura promedio
promedio = sum(temperaturas) / len(temperaturas)

# Recorre los días y muestra cuáles estuvieron por encima del promedio
for i in range(len(dias)):
    if temperaturas[i] > promedio:
        print(f"{dias[i]}: {temperaturas[i]}°C (por encima del promedio)")