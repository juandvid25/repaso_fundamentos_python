# Programa: Licencia de conducir con condiciones
# Descripción:
# Este programa verifica si una persona puede obtener
# la licencia de conducir según su edad y el permiso
# de sus padres.

# Variables
edad = 16
permiso_padres = True

# Comprueba si puede obtener la licencia
if edad >= 18:
    print("Puedes obtener la licencia de conducir.")
else:
    if edad >= 16:
        if permiso_padres:
            print("Puedes obtener la licencia con permiso de tus padres.")
        else:
            print("Necesitas el permiso de tus padres para obtener la licencia.")
    else:
        print("Eres demasiado joven para conducir.")