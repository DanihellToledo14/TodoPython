#Realizar un programa en el cual se declaren dos valores enteros por teclado utilizando el método __init__. Calcular después la suma, resta, multiplicación y división. Utilizar un método para cada una e imprimir los resultados obtenidos. Llamar a la clase Calculadora.

print("CALCULADORA PYTHON.(con init)")
class Calculadora():
    def __init__(self):
        self.num1 = int(input("Ingresar primer numero: "))
        self.num2 = int(input("Ingresar segundo numero: "))
    def suma(self):
        print("El resultado de la suma es ",self.num1 + self.num2)
    def resta(self):
        print("El resultado de la resta es ",self.num1 - self.num2)
    def multi(self):
        print("El resultado de la multiplicacion es ",self.num1 * self.num2)
    def division(self):
        print("El resultado de la division es ",self.num1 / self.num2)

cuenta = Calculadora()

cuenta.suma()
cuenta.resta()
cuenta.multi()
cuenta.division()
    