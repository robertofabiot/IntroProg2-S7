"""o Enunciado: Simula un cajero autom�tico con un saldo inicial. Permite al usuario 
realizar dep�sitos (sumar al saldo) y retiros (restar del saldo) hasta que decida salir. 
Muestra el saldo actual en cada operaci�n.
o Especificaci�n: Usa un bucle while, un acumulador (para el saldo), y contadores 
(opcionales, para el n�mero de dep�sitos/retiros). """

print("BIENVENIDO A SU CAJERO AUTOM�TICO")
saldo_inicial = float(input("Ingrese el saldo inicial: "))
saldo_actual = saldo_inicial
numero_depositos = 0
numero_retiros = 0

opcion = int(input("""
Seleccione una opci�n
[1] Dep�sito
[2] Retiro
[3] Salir
"""))

while opcion != 3:
    if opcion == 1:
        deposito = float(input("Ingrese el saldo a depositar: "))
        saldo_actual += deposito
        numero_depositos += 1
    elif opcion == 2:
        retiro = float(input("Ingrese el saldo a retirar: "))
        if retiro <= saldo_actual:
            saldo_actual -= retiro
            numero_retiros += 1
        else:
            print("Saldo insuficiente")
    else:
        print("Ingrese una opci�n v�lida.")

    print(f"Saldo actual: {saldo_actual}")
    opcion = int(input("""
Seleccione una opci�n
[1] Dep�sito
[2] Retiro
[3] Salir
"""))


print(f"""
GRACIAS POR USAR EL CAJERO
Saldo actual: {saldo_actual}
N�mero de dep�sitos: {numero_depositos}
N�mero de retiros: {numero_retiros}
""")