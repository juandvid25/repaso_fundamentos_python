# Programa: Licencia de conducir con elif
# Descripción:
# Este programa verifica si una persona puede obtener
# la licencia de conducir según su edad y si cuenta
# con el permiso de sus padres.

# Variables
edad = 16
permiso_padres = True

# Comprueba si cumple los requisitos
if edad >= 18:
    print("Puedes obtener la licencia de conducir.")
elif edad >= 16 and permiso_padres:
    print("Puedes obtener la licencia con permiso de tus padres.")
elif edad >= 16 and not permiso_padres:
    print("Necesitas el permiso de tus padres para obtener la licencia.")
else:
    print("Eres demasiado joven para conducir.")