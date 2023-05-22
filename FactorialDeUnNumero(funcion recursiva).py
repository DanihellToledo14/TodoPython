def Factorial(N):
    if N == 0:
        return 1
    else:
        return N * Factorial(N-1)

def Principal():
    num = int(input("Ingrese un numero positivo: "))
    if num < 0:
        print("El numero debe ser Positivo")
    else:
        print("El factorial de {} es {}".format(num, Factorial(num)))
        
Principal()

