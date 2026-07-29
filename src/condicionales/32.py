# Programa: Clasificación por edad con ternario anidado
# Descripción:
# Este programa utiliza operadores ternarios anidados
# para asignar una categoría según el rango de edad.

# Variable
edad = 20

# Asigna la categoría según la edad
categoria = "Menor" if edad < 18 else ("Joven Adulto" if edad < 30 else "Adulto")

# Muestra el resultado
print(categoria)