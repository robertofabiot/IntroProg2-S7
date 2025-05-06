""" Enunciado: Pide al usuario la cantidad N de números y luego solicita cada número. 
Encuentra el número mayor y el número menor. 
Especificación: Usa un bucle for, y acumuladores."""

n = int(input("Ingrese la cantidad de números: "))
numero_menor = None
numero_mayor = None

for i in range(1, n+1):
    x = int(input(f"Ingrese el número #{i}: "))
    
    if i == 1:
        numero_menor = x
        numero_mayor = x
    elif x < numero_menor:
        numero_menor = x
    elif x > numero_mayor:
        numero_mayor = x

print(f"El número mayor es {numero_mayor} y el número menor es {numero_menor}")