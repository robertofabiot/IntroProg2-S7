"""Leer una palabra diferente a fin y convertirla a mayúscula"""

palabra = input("Dime una palabra: ")
while palabra.lower() != "fin":
    print(f"{palabra.upper()} tiene {len(palabra)} letras")
    palabra = input("Dime una palabra: ")
else:
    print("Adiós...")






palabra = input("Dime una palabra: ")

for i in range (10000000):
    if(palabra.lower() == "fin"):
        break
    else:
        print(f"{palabra.upper()} tiene {len(palabra)} letras")
        palabra = input("Dime una palabra: ")