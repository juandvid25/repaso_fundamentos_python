# Programa: Juego para adivinar un número
# Descripción:
# Este programa genera un número aleatorio entre
# 1 y 10. El usuario tiene tres intentos para
# adivinarlo y recibe una pista después de
# cada intento fallido.

# Importa la librería para generar números aleatorios
import random

# Genera un número aleatorio entre 1 y 10
objetivo = random.randint(1, 10)

# Inicializa el contador de intentos
intentos = 0

# Variable que indica si el número fue adivinado
adivinado = False

# Repite el ciclo mientras no se adivine el número
# y aún queden intentos disponibles
while not adivinado and intentos < 3:

    # Incrementa el número de intentos
    intentos += 1

    # Solicita al usuario un número
    numero = int(input(f"Intento {intentos}/3: Adivina un número del 1 al 10: "))

    # Verifica si el número ingresado es correcto
    if numero == objetivo:
        print(f"¡Correcto! Has adivinado en {intentos} intentos.")
        adivinado = True
    else:
        # Indica si el número buscado es mayor o menor
        pista = "mayor" if numero < objetivo else "menor"
        print(f"Incorrecto. El número es {pista} que {numero}.")

# Muestra el número correcto si el usuario no lo adivinó
if not adivinado:
    print(f"Se acabaron los intentos. El número era {objetivo}.")