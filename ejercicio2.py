""" Pide al usuario un número entero positivo M y calcula el producto de los 
primeros M números pares."""

def calc_producto_pares(numero_m):
    if numero_m == 1:
        return f"El producto de los primeros {numero_m} números, tomando solo los pares, es 0"
    else:
        acumulador = 1
        contador = 2

    while contador <= numero_m:
        acumulador *= contador
        contador += 2

    return f"El producto de los primeros {numero_m} números, tomando solo los pares, es {acumulador}"

def main():
    while True:
        try:
            numero_m = int(input("Ingrese un número entero positivo: "))
            if numero_m < 0:
                print("Tiene que ingresar un número entero positivo.")
                continue
            break
        except ValueError:
            print("Tiene que ingresar un número entero.")
    
    print(calc_producto_pares(numero_m))
 
main()