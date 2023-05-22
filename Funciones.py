#Funciones

def funcion():
    print('Hola Mundo') 

funcion()
funcion()

#Funciones propias de python.

num = '70'
lista = [78, 86, 18, 22, 14]

print(type(num)) #Nos dice el tipo de elemento.
print(type(int(num)))#Transforma el elemento a entero.
print(type(float(num)))#Transforma el elemento a flotante.
print(len(lista))#Imprime la cantidad de elementos de la lista.
print(max(lista))#Imprime el mayor elemento de la lista.
print(min(lista))#Imprime el menor elemento de la lista.

#Funciones creadas.
#Sintaxis de funciones.

"""def <nombre de la funcion>():
    <sentencias>"""
    
#Ejemplo 1: Saludo.
    
def saludo():
    print('Hola Dani Toledo')
    print('Esta es otra sentencia')

saludo()
saludo()
saludo()
    
#Ejemplo 2: Tabla del 7.

'''def tabla7():
     for i in range(11):
         print('7 x {} = {}'.format(i, i * 7))

tabla7()'''

#Ejercicio 1: Crear un programa que tenga una lista, luego crear una funcion con la cual se van a pedir numeros al usuario para agregar a la lista. Debes crear una segunda funcion en donde se ordenen los numeros pares e impares dentro de dos listas nuevas

'''lista = []
num = 0

def pedir():
    i = 0
    while i <= 4:
        num = float(input('Escribe un numero: '))
        lista.append(num)
        i += 1

def ordenar():
    lista.sort()
    pares = []
    impares = []
    for i in lista:
        if i % 2 == 0:
            pares.append(i)
        else:
            impares.append(i)
    print(pares)
    print(impares)

pedir()
ordenar()'''

#Ejercicio 2: Escribir una función que reciba un número entero positivo y devuelva su factorial.

'''def factorial():
    factorial = 1
    num = int(input('Ingrese un numero positivo: '))
    if num < 0:
        print('ERROR INGRESO UN NUMERO EQUIVOCADO')
    else:
        for i in range(1,num + 1):
            factorial *= i
        print('El factorial de {} es {}'.format(num, factorial))
        
factorial()'''

'''Importando libreria(conjunto de funciones predeterminadas)
            
def factorial():
    from math import factorial
    num = int(input('Ingrese un numero positivo: '))
    if num < 0:
        print('ERROR INGRESO UN NUMERO EQUIVOCADO')
    else:
        print(factorial(num))

factorial()'''

#Funciones matematicas

import math
import random
print(math.pow(10, 2))#Tambien podemos imprimir la funcion sin importar la libreria. Seria: print(pow(10, 2)) = 100. De la manera con libreria el resultado lo da con decimal(100.0). Pow(numero, potencia): para elevar un numero.

print(math.sqrt(64))# sqrt: para la raiz cuadrada de un numero. sqrt(64) = 8.0

print(math.isqrt(64))# isqrt: para que el resultado de la raiz cuadrada este en entero. isqrt(64) = 8

print(math.sin(90))#Para sacar el seno del numero.
print(math.cos(90))#Para sacar el coseno del nunero.
print(math.tan(90))#Para sacar la tangente del numero.

print(random.randint(1, 100))#Para imprimir un numero al azar dentro de los parametros.

#Retorno de datos

#Sintaxis
'''def <nombre>():
    <sentencias>
    return  '''

def entero():
    print('Este es un numero entero: ')
    return 10
    
def decimal():
    print('Este es un numero decimal: ')
    return 90.99
    
def mensaje():
    return 'Este es el mensaje'
    
print(entero())
entero()#Si llamo a la funcion sin imprimirla me imprime la funcion sin el retorno.
print(decimal())
print(mensaje())

