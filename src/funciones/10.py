# Programa: Creación de un perfil de usuario
# Descripción:
# Este programa define una función que crea un perfil de usuario
# utilizando nombre, edad y ciudad. Si no se especifica la ciudad,
# se asigna "Madrid" como valor predeterminado.

def crear_perfil(nombre, edad, ciudad="Madrid"):
    return f"Perfil: {nombre}, {edad} años, {ciudad}"