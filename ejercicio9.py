# Calcular la frecuencia de cada dígito en un número 
# o Enunciado: Pide al usuario un número entero y calcula cuántas veces aparece cada 
# dígito (0 al 9) en el número. 
# o Especificación: Usa un bucle while y un array/list de contadores (uno para cada 
# dígito).

def calcular_frecuencia(numero):
    lista_numeros = [0] * 10
    while numero > 0:
        digito = numero % 10
        lista_numeros[digito] += 1
        numero //= 10
    for i in range(10):
        print(f"Frecuencia de {i}: {lista_numeros[i]}")        

def main():
    while true:
        try:
            numero = int(input("Ingrese un número entero: "))
            numero = abs(numero)
        except TypeError:
            print("Tiene que ingresar un número entero. No sea imbécil.")
    calcular_frecuencia(numero)

main()
