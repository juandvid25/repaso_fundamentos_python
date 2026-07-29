# Programa: Finalizar un ciclo con la instrucción break
# Descripción:
# Este programa recorre los números del 1 al 10.
# Cuando encuentra el número 5, muestra un mensaje
# y finaliza el ciclo utilizando la instrucción break.

# Recorre los números del 1 al 10
for numero in range(1, 11):

    # Verifica si el número actual es 5
    if numero == 5:
        print("¡Encontrado el 5! Saliendo del bucle...")

        # Finaliza el ciclo
        break

    # Muestra el número actual
    print(f"Número actual: {numero}")