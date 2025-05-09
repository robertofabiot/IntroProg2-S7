"""o Enunciado: Simula un cajero automático con un saldo inicial. Permite al usuario 
realizar  (sumar al saldo) y retiros (restar del saldo) hasta que decida salir. 
Muestra el saldo actual en cada operaci�n.
o Especificaci�n: Usa un bucle while, un acumulador (para el saldo), y contadores 
(opcionales, para el número de /retiros). """

def deposito(saldo_actual, numero_depositos):
    deposito = float(input("Ingrese el saldo a depositar: "))
    saldo_actual += deposito
    numero_depositos += 1
    return saldo_actual, numero_depositos

def retiro(saldo_actual, numero_retiros):
    retiro = float(input("Ingrese el saldo a retirar: "))
    if retiro <= saldo_actual:
        saldo_actual -= retiro
        numero_retiros += 1
    else:
        print("Saldo insuficiente")
    return saldo_actual, numero_retiros

def salir(saldo_actual, numero_depositos, numero_retiros):
    print(f"""
GRACIAS POR USAR EL CAJERO
Saldo actual: {saldo_actual}
Número de depósitos: {numero_depositos}
Número de retiros: {numero_retiros}
""")

def main():
    print("BIENVENIDO A SU CAJERO AUTOMÁTICO")
    saldo_inicial = float(input("Ingrese el saldo inicial: "))
    saldo_actual = saldo_inicial
    numero_depositos = 0
    numero_retiros = 0

    opcion = int(input("""
Seleccione una opción
[1] Depósito
[2] Retiro
[3] Salir
"""))

    while opcion != 3:
        if opcion == 1:
            saldo_actual, numero_depositos = deposito(saldo_actual, numero_depositos)
        elif opcion == 2:
            saldo_actual, numero_retiros = retiro(saldo_actual, numero_retiros)
        else:
            print("Ingrese una opción válida.")

        print(f"Saldo actual: {saldo_actual}")
        opcion = int(input("""
Seleccione una opción
[1] Depósito
[2] Retiro
[3] Salir
"""))

    salir(saldo_actual, numero_depositos, numero_retiros)

main()