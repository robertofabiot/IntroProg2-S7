import datetime
import random
import time as t
import os

fecha = datetime.date.today()

print(f"Bienvenido \n{fecha}")

def esperar(espera):
    while(espera >= 0):
        os.system("cls || clear")
        print(f"Espera {espera}")
        espera-=1
        t.sleep(1)
    os.system("cls||clear")
    
def adivinar(num_user, num_rdn):
    esperar(2)
    if num_user == num_rdn:
        os.system("color 2a")
        print("Adivinaste")
    else:
        os.system("color 47")
        print("Lo siento, no es el número.")
        
def main():
    num_alea = random.randint(1, 10)
    resp = "s"
    while resp.lower() != "n":
        num = input("Ingresa un número del 1 al 10: ")
        adivinar(int(num), num_alea)
        resp = input("Desea seguir jugando? [S = Si - N = No - R = Reiniciar partida]: ")
        if resp.lower() == "r":
           num_alea = random.randint(1, 10) 
        
main()  