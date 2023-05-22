class FabricaTelefonos():
    
    def __init__(self, marca, color):
        self.marca = marca
        self.color = color
        print('El objeto {} ha sido creado'.format(self.marca)) #Metodo __init__: Se ejecuta al crearse el objeto. (Metodo Constructor)
    def __str__(self):
        return 'El objeto es {}'.format(self.marca) #Metodo __str__: Se ejecuta para cambiar el texto del espacio de memoria.
        
    def __del__(self):
        print('El objeto {} ha sido destruido'.format(self.marca)) #Metodo __del__: Se ejecuta al finalizar el codigo y elimina el objeto.

telefono = FabricaTelefonos('Nokia', 'Negro')

#print(telefono.marca)
print(telefono)