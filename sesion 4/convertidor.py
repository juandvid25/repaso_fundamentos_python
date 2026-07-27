# Programa: Conversión entre millas y kilómetros
# Autor: Juan David
# Descripción:
# Este programa convierte una distancia en millas a kilómetros
# y una distancia en kilómetros a millas, mostrando los resultados
# redondeados a dos decimales.

# Se declara una distancia en kilómetros.
kilometers = 12.25

# Se declara una distancia en millas.
miles = 7.38

# Convierte las millas a kilómetros.
# 1 milla equivale a 1.61 kilómetros.
miles_to_kilometers = miles * 1.61

# Convierte los kilómetros a millas.
# 1 kilómetro equivale a 1 / 1.61 millas.
kilometers_to_miles = kilometers / 1.61

# Muestra el resultado de la conversión de millas a kilómetros.
# La función round() redondea el resultado a dos decimales.
print(miles, "millas son", round(miles_to_kilometers, 2), "kilómetros")

# Muestra el resultado de la conversión de kilómetros a millas.
# La función round() redondea el resultado a dos decimales.
print(kilometers, "kilómetros son", round(kilometers_to_miles, 2), "millas")






# Este programa convierte una cantidad de dólares estadounidenses (USD)
# a euros (EUR) utilizando una tasa de cambio fija.

# Se declara la cantidad de dinero en dólares estadounidenses.
usd = 100

# Se realiza la conversión de dólares a euros.
# En este ejemplo, 1 USD equivale a 0.88 EUR.
eur = usd * 0.88

# Muestra un título en la consola.
print("Conversión de Moneda")

# Muestra el resultado de la conversión.
# La función round() redondea el valor a dos decimales.
print(usd, "USD son", round(eur, 2), "EUR")