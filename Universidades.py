#Crear un programa con tres clases Universidad, con atributos nombre (Donde se almacena el nombre de la Universidad). Otra llamada Carerra, con los atributos especialidad (En donde me guarda la especialidad de un estudiante). Una ultima llamada Estudiante, que tenga como atributos su nombre y edad. El programa debe imprimir la especialidad, edad, nombre y universidad de dicho estudiante con un objeto llamado persona.

class Universidad():
    def __init__(self, nombreU):
        self.nombreU = nombreU

class Carrera():
    def carrera(self, espe):
        self.espe = espe
        
class Estudiante(Universidad,Carrera):
    def datos(self, nombreE, edad):
        self.nombreE = nombreE
        self.edad = edad
        print("El nombre del estudiante es {} y su edad es {}, estudia la carrera de {} en la universidad {}.".format(self.nombreE, self.edad, self.espe, self.nombreU))
        

estudiante = Estudiante("UTN")
estudiante.carrera("Programacion")
estudiante.datos("Daniel", 29)
