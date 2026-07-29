# Programa: Cálculo de estadísticas básicas
# Descripción:
# Este programa define una función que calcula la suma,
# el promedio, el valor mínimo y el valor máximo de una
# lista de números, devolviendo todos los resultados.

def estadisticas(numeros):
    total = sum(numeros)
    promedio = total / len(numeros)
    minimo = min(numeros)
    maximo = max(numeros)

    return total, promedio, minimo, maximo

datos = [4, 8, 15, 16, 23, 42]

suma, media, menor, mayor = estadisticas(datos)

print(suma)
print(media)
print(menor)
print(mayor)