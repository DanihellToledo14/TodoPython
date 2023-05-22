print(" Ejercicio 1: Mensaje en tres lineas.")
print()
print('''    "La felicidad puede ser encontrada hasta en los mas oscuros
     momentos, si somo capaces de usar bien la luz".
     -Albus Dombuldor. ''')

print()
print(" Ejercicio 2: Mensaje.")
print()     
saludo = "    ¡Hola Mundo!"
print(saludo)

print()
print(' Ejercicio 3: Nombre y Apellido.')
print()
print('    ¿Cuál es tu nombre y apellido?')
print()
nombre = input("    Ingresar solo nombres: ")
apellido = input("    Ingresar solo apellidos: ")
print()
#Ejemplo con formato f''
print(f"    Hola {nombre} {apellido}, mucho gusto de conocerte.")
#Ejemplo con formato %s 
print("    Hola %s %s, gusto de conocerte." %(nombre,apellido))

print()
print(" Ejercicio 4: Suma de numeros.")
print()

suma = 0
num1 = int(input('    Introducir un numero entero positivo: '))
if num1 < 0:
    print('    ¡Imposible! El numero es negativo.')
elif num1 == 0:
    print('    Escriba un número mayor a 0')
else:
    suma = int(num1*(num1+1)/2)
#Ejemplo con formato format()
print('    La suma de los numeros es: {}'.format(suma))

print()
print(" Ejercicio 5: Area de un cuadrado.")
print()

lado = float(input("    Ingresar el valor del lado del cuadrado: "))
AreaC = lado**2
#Ejemplo con formato concatenando
print("    El area del cuadrado es: ", AreaC)

print()
print(" Ejercicio 6: Area de un Triangulo")
print()

base = float(input("    Ingresar el valor de la base del Triangulo: "))
altura = float(input("    Ingresar el valor de la altura del triangulo: "))
AreaT = base*altura/2
#Ejemplo con formato concatenando
print("    El area del Triangulo es: " + str(AreaT))

print()
print(" Ejercicio 7: Area de un circulo")
print()
PI = 3.1416
radio = float(input("    Ingresar el valor del radio del circulo: "))
AreaCir = PI*(radio**2)
#Ejemplo con formato concatenando
print("    El area del circulo es: %0.2f"%(AreaCir))

print()
print('Ejercicio 8: Temperatura')
print()

f = float(input('    Ingresar grados fahrenheit (F°): '))

C = (f-32)*5/9
print('    El valor en celsius de %0.2fF° es: %0.2f C°'%(f,C))
print()
C2 = float(input('    Ingresar grados celcius (C°): '))

f2 = (C2*(9/5))+32
print('    El valor en fahrenheit de %0.2fC° es: %0.2f F°'%(C2,f2))