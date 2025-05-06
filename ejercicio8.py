""" Enunciado: Pide al usuario la cantidad N de n�meros y luego solicita cada n�mero. 
Encuentra el n�mero mayor y el n�mero menor. 
Especificaci�n: Usa un bucle for, y acumuladores."""

n = int(input("Ingrese la cantidad de n�meros: "))
numero_menor = None
numero_mayor = None

for i in range(1, n+1):
    x = int(input(f"Ingrese el n�mero #{i}: "))
    
    if i == 1:
        numero_menor = x
        numero_mayor = x
    elif x < numero_menor:
        numero_menor = x
    elif x > numero_mayor:
        numero_mayor = x

print(f"El n�mero mayor es {numero_mayor} y el n�mero menor es {numero_menor}")