#Realizar un programa que conste de una clase llamada Estudiante, que tenga como atributos el nombre y la nota del alumno. Definir los métodos para inicializar sus atributos, imprimirlos y mostrar un mensaje con el resultado de la nota y si ha aprobado o no.

class Estudiante():
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
    def imprimir(self):
        if self.nota >= 7:
            print("El alumno {} a aprobado con una nota de {}.".format(self.nombre, self.nota))
        else:
            print("El alumno {} a desaprobado con una nota de {}.".format(self.nombre, self.nota))
            
estudiante1 = Estudiante("Daniel", 9)
estudiante1.imprimir() 

estudiante2 = Estudiante("Mathiaz", 5)
estudiante2.imprimir()