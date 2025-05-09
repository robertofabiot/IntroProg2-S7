""" Enunciado: Pide al usuario la cantidad N de n�meros y luego solicita cada n�mero. 
Encuentra el n�mero mayor y el n�mero menor. 
Especificaci�n: Usa un bucle for, y acumuladores."""

def encontrar_mayor_menor(numeros):    
    numero_menor = None
    numero_mayor = None

    for i in range(1, numeros+1):
        x = int(input(f"Ingrese el número #{i}: "))

        if i == 1:
            numero_menor = x
            numero_mayor = x
        elif x < numero_menor:
            numero_menor = x
        elif x > numero_mayor:
            numero_mayor = x

    print(f"El número mayor es {numero_mayor} y el número menor es {numero_menor}")

def main():
    while True:
        try:
            numeros = int(input("Ingrese la cantidad de números: "))
            if numeros <= 0:
                raise ValueError
            break
        except ValueError:
            print("ERROR. La cantidad de números debe ser positiva y entera.")
        

    encontrar_mayor_menor(numeros)

main()