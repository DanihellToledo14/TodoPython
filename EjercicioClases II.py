#Crear una clase llamada Fabrica que tenga los atributos Llantas, Color, Precio; luego crear dos clases mas que hereden de Fabrica, las cuales son Moto y Carro. Crear metodos que muestren cantidad de llantas, color y precio de ambos transportes. Por ultimo, crear objetos para cada clase y mostrar por pantalla atributos de cada uno.

class Fabrica(): #Clase Padre.
    def __init__(self, llantas, color, precio): #Metodo constructor.
        self.llantas = llantas #Atributo.
        self.color = color #Atributo.
        self.precio = precio #Atributo.
        
class Moto(Fabrica): #Clase hija.
    def datos(self): #Metodo de instancia.
        print("La cantidad de llantas de la moto es de: ",self.llantas)
        print("El color de la moto es: ",self.color)
        print("El precio de la moto es: $",self.precio)

class Carro(Fabrica): #Clase hija.
    def datos(self): #Metodo de instancia.
        print("La cantidad de llantas del carro es de: ",self.llantas)
        print("El color del carro es: ",self.color)
        print("El precio del carro es: $",self.precio)
        

Moto1 = Moto(2,"Negro", 4000) #Objeto.
Moto1.datos() #Mostrar atributos.

Carro1 = Carro(4,"Azul", 20000) #Objeto.
Carro1.datos() #Mostrar atributos.
