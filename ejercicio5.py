num = int(input("Ingresa un n�mero entero positivo: "))
i = 1
acumulador = 1

while i <= num:
     acumulador *= i
     i+=1

print(acumulador)