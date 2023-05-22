#Escriba un programa que pida un número de dados y muestre los valores de ese número de dados, al azar.

import random

def main():
    print("TIRADA DE DADOS")
    numero = int(input("Número de dados: "))
    if numero < 1:
        print("¡Imposible!")
    else:
        print("Dados: ", end="")
        for _ in range(numero):
            print(f"{random.randrange(1, 7)} ", end="")


main()