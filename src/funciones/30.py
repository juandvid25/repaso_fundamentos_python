# Programa: Clasificación de una puntuación
# Descripción:
# Este programa determina la calificación correspondiente
# a una puntuación entre 0 y 100.

# Función que devuelve la calificación según la puntuación
def obtener_calificacion(puntuacion):

    # Verifica que la puntuación sea válida
    if puntuacion < 0 or puntuacion > 100:
        return "Puntuación inválida"

    # Clasifica la puntuación
    if puntuacion >= 90:
        return "Sobresaliente"

    if puntuacion >= 70:
        return "Notable"

    if puntuacion >= 60:
        return "Bien"

    if puntuacion >= 50:
        return "Suficiente"

    # Si no cumple ninguna condición anterior
    return "Insuficiente"