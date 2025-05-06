""" Pide al usuario un número entero positivo M y calcula el producto de los 
primeros M números pares."""

m = int(input("Ingrese un número entero positivo: "))
acumulador = 1
contador = 2

while contador <= m:
    acumulador *= contador
    contador += 2

print(acumulador)