"""Enunciado: Pide al usuario una cadena y cuenta cuántas vocales (a, e, i, o, u) tiene.
o Especificación: Usa un bucle for para recorrer la cadena y contadores para cada 
vocal."""

def contar_vocales(cadena):
    contador = 0
    cadena = cadena.lower()

    for caracter in cadena:
        if caracter == "a" or caracter == "e" or caracter == "i" or caracter == "o" or caracter == "u":
            contador += 1

    print(f"Las vocales en el texto son: {contador}")

def main():
    cadena = input("Ingrese un texto: ")
    contar_vocales(cadena)

main()