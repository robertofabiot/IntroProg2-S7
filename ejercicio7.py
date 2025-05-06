""" Enunciado: Pide al usuario una lista de números (pueden ser ingresados uno a la 
vez hasta que el usuario ingrese un valor de fin, como 0 o -1). Calcula la suma de 
los números pares y la suma de los números impares.
o Especificación: Usa un bucle while, acumuladores para la suma de pares e impares, 
y un contador (opcional, dependiendo de la implementación)."""

x = 0
suma_pares = 0
suma_impares = 0

x = int(input("Ingrese un número. Ingrese 0 para finalizar: "))

while x != 0:
    if x % 2 == 0: #numero par
        suma_pares += x
    else:
        suma_impares += x
    x = int(input("Ingrese un número. Ingrese 0 para finalizar: "))

print(f"La suma de los pares es {suma_pares} y la de los impares es {suma_impares}")