# Programa: Validar una lista de edades
# Descripción:
# Este programa define una función que verifica
# si todas las edades de una lista son válidas.
# Si encuentra una edad inválida, detiene el
# recorrido; de lo contrario, confirma que
# todas las edades son correctas.

# Función que valida las edades de una lista
def validar_edades(lista_edades):

    # Recorre cada edad de la lista
    for edad in lista_edades:

        # Verifica si la edad no es un número entero o es negativa
        if not isinstance(edad, int) or edad < 0:
            print(f"Edad inválida encontrada: {edad}")

            # Finaliza el ciclo al encontrar un dato inválido
            break

    # Se ejecuta únicamente si el ciclo termina sin ejecutar break
    else:
        print("Todas las edades son válidas")
        return True

    # Devuelve False si se encontró una edad inválida
    return False