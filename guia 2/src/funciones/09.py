# Programa: Función con parámetro opcional
# Descripción:
# Este programa define una función para saludar a una persona.
# El mensaje de bienvenida es opcional y tiene un valor por
# defecto, aunque también puede personalizarse.

def saludar(nombre, mensaje="¡Bienvenido!"):
    print(f"Hola {nombre}. {mensaje}")

saludar("Carlos")
saludar("María", "¿Cómo estás hoy?")