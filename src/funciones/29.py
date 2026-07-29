# Programa: Cálculo del promedio de una lista
# Descripción:
# Este programa calcula el promedio de una lista de números
# utilizando una función.

# Función que calcula el promedio de una lista
def calcular_promedio(numeros):
    return sum(numeros) / len(numeros)

# Lista de notas
notas = [7, 8, 6, 9]

# Llamada a la función para calcular el promedio
promedio = calcular_promedio(notas)

# Muestra el promedio obtenido
print(promedio)