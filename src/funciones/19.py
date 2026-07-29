# Programa: Función sin valor de retorno
# Descripción:
# Este programa define una función que imprime un saludo
# personalizado. Como la función no utiliza la instrucción
# return, el valor devuelto es None.

def saludar(nombre):
    print(f"Hola, {nombre}")

resultado = saludar("Laura")

print(f"La función devolvió: {resultado}")