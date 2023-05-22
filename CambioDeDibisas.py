print('***CAMBIO DE DIVISAS***')
def USA(*Change):
    dolar = {'ARG': 462.32, 'EU': 0.900}
    return Change[1]/dolar[Change[0].upper()]

def EU(*Change):
    euro = {'ARG': 236.407, 'USA': 1.111 }
    return Change[1]/euro[Change[0].upper()]

def ARG(*Change):
    peso = {'USA': 0.00216, 'EU': 0.00423 }
    return Change[1]/peso[Change[0].upper()]
    
def carga_datos(): 
    monedatienes = input("¿Que moneda tienes? -> ARG = Peso Arg, USA = Dolar USA, EU = Euro : ")
    montotienes = float(input("Ingrese que monto desea cambiar: "))
    if monedatienes.upper() == 'USA':
        monedacambiar = input("Ingrese la moneda a cambiar ARG o EU: ")
    elif monedatienes.upper() == 'EU':
        monedacambiar = input("Ingrese la moneda a cambiar ARG o USA: ")
    else:
        monedacambiar = input("Ingrese la moneda a cambiar EU o USA: ")
        
    return monedatienes, montotienes, monedacambiar.upper()
    
def imprimir(montocambiado, monedacambio):
    print("El monto cambiado es: {:.3f}".format(montocambiado), monedacambio)

def Cambio():
    cambio = 's'
    while cambio == 's':
        datos = carga_datos()
        
        if datos[2] == 'USA':
                montocambiado = USA(datos[0], datos[1])
                imprimir(montocambiado,datos[2])
        elif datos[2] == 'ARG':
                montocambiado = ARG(datos[0], datos[1])
                imprimir(montocambiado,datos[2])
        else:
                montocambiado = EU(datos[0], datos[1])
                imprimir(montocambiado, datos[2])
                   
        cambio = input('Desea hacer otro cambio de divisas? s/n ')

Cambio()
        
    