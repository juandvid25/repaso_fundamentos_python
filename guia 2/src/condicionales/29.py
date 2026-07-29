# Programa: Encontrar el número mayor
# Descripción:
# Este programa compara tres números y almacena
# el mayor de ellos en una variable.

# Variables
a = 5
b = 10
c = 15

# Inicializa la variable con el primer valor
mayor = a

# Comprueba si b es mayor
if b > mayor:
    mayor = b

# Comprueba si c es mayor
if c > mayor:
    mayor = c

# Muestra el resultado
print(f"El número mayor es {mayor}.")