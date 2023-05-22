print('Ejercicio 11: Positivos y negativos.')
print()

#Solicitud del numero.
num = int(input('    Ingresa un numero entero: '))

#Inicio de programa.
#Condiciones para saber si el numero es positivo o negativo.
if num > 0:
    print('    El numero %0.2f es positivo.'%(num))
elif num == 0:
    print('    El numero %0.2f no es positivo ni negativo.'%(num))
else:
    print('    El numero %0.2f es negativo.'%(num))
    
print()
print('Ejercicio 12: Dos personas cual es la mayor.')
print()

#Solicitud de las edades.
edad1 = int(input('    Ingresa la edad de la primer persona: '))
edad2 = int(input('    Ingresa la edad de la segunda persona: '))

#Inicio de programa.
#Condiciones para saber quien es mayor.
if edad1 > edad2:
    print(f'    La primera persona es la mayor con {edad1} años.')
elif edad1 == edad2:
    print(f'    Ambos tienen {edad1} años.')
else:
    print(f'    La segunda persona es la mayor con {edad2} años.')
    
print()
print('Ejercicio 13: Numeros pares e impares.')
print()

#Ingreso de numero por teclado.
num = int(input('    Ingresa un numero: '))

#Inicio del programa.
#Condiciones para saber si es par o impar.

if num % 2 == 0:
    print('    El numero {} es par.'.format(num))
else:
    print('    El numero {} es impar.'.format(num))
    
if num == (num // 2) * 2:
    print('    El numero %d es par.'%(num))
else:
    print(f'    El numero {num} es impar.')

print()
print('Ejercicio 14: Multiplo de 3.')
print()

# Ingreso de numero por teclado.
num = int(input('    Ingrese un numero: '))

if num == (num // 3) * 3:
    print("    El numero %d es multiplo de 3." %(num))
else:
    print("    El numero %d no es multiplo de 3." %(num))

print()
print('Ejercicio 15: Mayusculas y minusculas.')
print()

#Solicitud de Datos.
letra = input('    Ingrese una letra: ')

#Inicio del programa.
#Condiciones para saber si es mayuscula o minuscula.
if letra <= 'z'  and letra >= 'a':  # a-z (97-122)
    print(f'    La letra {letra} es minuscula.')

elif letra <= 'Z' and letra >= 'A':  # A-Z (65-90)
    print('    La letra %d es Mayuscula.'%(letra))
else:
    print('    El valor introducido no es una letra.')
    
print()
print('Ejercicio 16: El mayor de 3 numeros.')
print()

#Solicitud de datos
num1  = float(input('    Ingrese el primer  numero: '))
num2 = float(input('    Ingrese el segundo numero: '))
num3  = float(input('    Ingrese el tercer  numero: '))

#Inicio del programa.
if num1 > num2:
    if num1 > num3:
        max = num1
    else:
        max = num3
else:
    if num2 > num3:
        max = num2
    else:
        max = num3

print('    El numero %5.2f es el mayor.' %(max))

print()
print('Ejercicio 17: El mayor de 5 numeros.')
print()

#Solicitud de datos.
num1  = float(input('    Ingrese el primer  numero: '))
num2 = float(input('    Ingrese el segundo numero: '))
num3  = float(input('    Ingrese el tercer  numero: '))
num4  = float(input('    Ingrese el cuarto  numero: '))
num5  = float(input('    Ingrese el quinto  numero: '))

#Inicio del programa.
max_pos = num1

if num2 > max_pos:
    max_pos = num2

if num3 > max_pos:
    max_pos = num3

if num4 > max_pos:
    max_pos = num4

if num5 > max_pos:
    max_pos = num5

max = max_pos

print ('    El Numero %5.2f es el mayor.'%(max))