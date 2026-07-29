# Programa: Determinar el número mayor
# Descripción:
# Este programa compara tres números e identifica
# cuál de ellos es el mayor utilizando estructuras
# condicionales anidadas.

# Variables
a = 5
b = 10
c = 15

# Compara los tres números
if a > b:
    if a > c:
        print("a es el mayor.")
    else:
        if c > b:
            print("c es el mayor.")
        else:
            print("b es el mayor.")
else:
    if b > c:
        print("b es el mayor.")
    else:
        print("c es el mayor.")