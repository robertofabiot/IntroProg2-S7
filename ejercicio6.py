def calc_palabras(cadena):
    contador = 1
    
    for caracter in cadena:
        if caracter == " ":
            contador += 1
    
    print(f"Las palabras en el texto son: {contador}")

def main():
    cadena = input("Ingrese un texto: ")
    calc_palabras(cadena)

main()