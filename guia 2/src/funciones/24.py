# Programa: Formato de nombres
# Descripción:
# Este programa recibe un nombre y un apellido,
# formatea ambos y muestra el resultado.

# Función que da formato al nombre completo
def formato_nombre(nombre, apellido):
    return f"{apellido.upper()}, {nombre.capitalize()}"

# Muestra el nombre formateado
print(formato_nombre("ana", "garcía"))