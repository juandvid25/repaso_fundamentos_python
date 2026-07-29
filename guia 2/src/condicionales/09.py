# Programa: Clasificar una calificación
# Descripción:
# Este programa asigna una categoría según
# el valor de una nota.

# Variable que almacena la nota
nota = 87

# Clasifica la nota
if nota >= 90:
    print("Calificación: Sobresaliente")
elif nota >= 80:
    print("Calificación: Notable")
elif nota >= 70:
    print("Calificación: Aprobado")
else:
    print("Calificación: Suspenso")