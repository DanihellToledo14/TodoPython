print('Calculadora Python.')
class Calculadora():
    def __init__(self):
        self.num1 = int(input("Ingresa el primer numero: "))
        self.num2 = int(input("Ingresa el segundo numero: "))
        
    def sumar(self):
        self.suma = self.num1 + self. num2
        print("El resultado de la suma es:",self.suma)
        
    def restar(self):
        self.resta = self.num1 - self. num2
        print("El resultado de la resta es:",self.resta)
        
    def multi(self):
        self.multi = self.num1 * self. num2
        print("El resultado de la multiplicacion es:",self.multi)
    def division(self):
        self.div = self.num1 / self. num2
        print("El resultado de la division es:", self.div)


calcular = Calculadora()
calcular.sumar()
calcular.restar()
calcular.multi()
calcular.division()