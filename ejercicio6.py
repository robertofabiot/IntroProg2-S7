cadena = input("Ingrese un texto: ")
contador = 1

for caracter in cadena:
    if caracter == " ":
        contador += 1

print(f"Las palabras en el texto son: {contador}")
