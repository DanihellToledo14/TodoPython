#Mayores que el primero
print('MAYOR QUE EL PRIMERO')
num1 = int(input('¿Cúantos valores va a introducir?: '))
if num1 < 0:
    print('¡Imposible!') 
else:
    num2 = int(input('Escriba un numero: '))
    for i in range(num1-1):
        num3 = int(input('Escriba un numero mayor a {}: '.format(num2)))
        if num2 > num3:
            print('¡{} no es mayor a {}!'.format(num3, num2))
print('Gracias por su colaboración')
        