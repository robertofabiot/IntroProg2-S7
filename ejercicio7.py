""" Enunciado: Pide al usuario una lista de n�meros (pueden ser ingresados uno a la 
vez hasta que el usuario ingrese un valor de fin, como 0 o -1). Calcula la suma de 
los n�meros pares y la suma de los n�meros impares.
o Especificaci�n: Usa un bucle while, acumuladores para la suma de pares e impares, 
y un contador (opcional, dependiendo de la implementaci�n)."""

def calc_pares_impares(x):
    suma_pares = 0
    suma_impares = 0

    while x != 0:
        if x % 2 == 0: #numero par
            suma_pares += x
        else:
            suma_impares += x
        x = int(input("Ingrese un número. Ingrese 0 para finalizar: "))

    print(f"La suma de los pares es {suma_pares} y la de los impares es {suma_impares}")

def main():
    while True:
        try:
            x = int(input("Ingrese un número. Ingrese 0 para finalizar: "))
            break
        except ValueError:
            print("Tiene que ingresar un valor entero")
            
    calc_pares_impares(x)

main()