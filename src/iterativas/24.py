# Programa: Buscar un número primo con for...else
# Descripción:
# Este programa recorre una lista de números en
# busca de un posible número primo. Si lo encuentra,
# finaliza el ciclo con break; de lo contrario,
# ejecuta el bloque else al terminar el recorrido.

# Lista de números
numeros = [4, 6, 8, 9, 10, 12]

# Recorre la lista de números
for num in numeros:

    # Verifica si el número no es divisible entre 2 ni entre 3
    if num % 2 != 0 and num % 3 != 0:

        # Muestra el número encontrado y finaliza el ciclo
        print(f"¡Encontrado un primo: {num}!")
        break

# Se ejecuta únicamente si el ciclo termina sin encontrar un número
# que cumpla la condición y, por tanto, sin ejecutar break
else:
    print("No se encontró ningún número primo en la lista")