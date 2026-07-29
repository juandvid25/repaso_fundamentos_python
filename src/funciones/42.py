# Programa: Generación de una contraseña aleatoria
# Descripción:
# Este programa genera una contraseña aleatoria utilizando
# letras, números y caracteres especiales.

# Función que genera una contraseña aleatoria
def generar_contraseña(longitud=8):
    """
    Genera una contraseña aleatoria.
    """

    # Importa los módulos necesarios
    import random
    import string

    # Conjunto de caracteres disponibles
    caracteres = (
        string.ascii_letters
        + string.digits
        + string.punctuation
    )

    # Genera y devuelve la contraseña aleatoria
    return "".join(
        random.choice(caracteres)
        for _ in range(longitud)
    )