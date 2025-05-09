"""Suma de los primeros N números 
o Enunciado: Pide al usuario un número entero positivo N y calcula la suma de los 
números desde 1 hasta N. 
o Especificación: Usa un bucle for y un acumulador."""

def calc_suma(num):
    suma = 0
    for i in range (1, num+1):
        suma += i
    return suma

def main():
    while True:
        try:
            num = int(input("Ingrese un número entero: "))
            num = abs(num)
            break
        except ValueError:
            print("Tiene que ingresar un número entero.")
    print(f"La suma es {calc_suma(num)}")
    
main()