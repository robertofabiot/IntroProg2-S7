def calc_factorial(num):     
     i = 1
     acumulador = 1

     while i <= num:
          acumulador *= i
          i += 1

     print(f"El factorial de {num} es: {acumulador}")

def main():
     while True:
          try:
               num = int(input("Ingresa un número entero positivo: "))
               if num <= 0:
                    raise ValueError
               break
          except ValueError:
               print("ERROR. Tiene que ingresar un número entero y positivo.")

     calc_factorial(num)
     
main()