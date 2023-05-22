#Sumar digitos de un numero de manera recursiva.

def Sumadigitos(Numero):
    if Numero == 0:
        return 0
    else:
        digito = Numero % 10
        return digito + Sumadigitos(Numero // 10)

def Principal():
    Numero = int(input("Ingrese un numero: "))
    if Numero < -9 or Numero > 9:
        print("La suma de los digitos del {} es {}.".format(Numero, Sumadigitos(abs(Numero))))
    else:
        print("El numero es de un solo digito.", str(Numero))
        
Principal()