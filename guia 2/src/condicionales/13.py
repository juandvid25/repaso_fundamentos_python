# Programa: Identificar la ubicación de un punto
# Descripción:
# Este programa utiliza match-case para determinar
# la posición de un punto en el plano cartesiano.

# Variable que almacena las coordenadas
punto = (0, 0)

# Evalúa la posición del punto
match punto:
    case (0, 0):
        print("El punto está en el origen.")
    case (0, y):
        print(f"El punto está en el eje Y en y={y}.")
    case (x, 0):
        print(f"El punto está en el eje X en x={x}.")
    case (x, y):
        print(f"El punto está en coordenadas x={x}, y={y}.")