num = int(input("Ingresa un número entero positivo: "))
i = 1
acumulador = 1

while i <= num:
     acumulador *= i
     i+=1

print(acumulador)