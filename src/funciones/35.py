# Programa: Validación de un correo electrónico
# Descripción:
# Este programa define una función que verifica si una
# dirección de correo electrónico tiene un formato válido.

# Función que valida el formato de un correo electrónico
def validar_email(email):
    """
    Verifica si una dirección de correo electrónico tiene formato válido.
    """

    # Verifica que el dato recibido sea una cadena de texto
    if not isinstance(email, str):
        raise TypeError("El email debe ser una cadena de texto")

    # Comprueba que el correo contenga '@' y un dominio válido
    return "@" in email and "." in email.split("@")[-1]