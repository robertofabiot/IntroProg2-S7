"""Enunciado: Pide al usuario la cantidad N de calificaciones y luego solicita cada 
calificación. Calcula el promedio de las calificaciones ingresadas.
o Especificación: Usa un bucle for para leer las calificaciones, un acumulador para la 
suma, y un contador para la cantidad."""

def calc_promedio(n):
    acumulador = 0

    for i in range (1, n+1):
        calificacion = float(input(f"Ingrese la calificación #{i}: "))
        acumulador += calificacion

    print(f"El promedio es: {(acumulador/n):.2f}")

def main():
    while True:
        try:
            n = int(input("Ingrese la cantidad de calificaciones: "))
            if n <= 0:
                raise ValueError
            break
        except ValueError:
            print("Tiene que ingresar un número entero positivo.")
    calc_promedio(n)

main()