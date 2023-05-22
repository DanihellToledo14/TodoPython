#Mayores al ultimo: 
print('MAYORES QUE EL ANTERIOR')
num1 = int(input('¿Cúantos valores va a introducir?: '))
if num1 < 0:
    print('¡Imposible!') 
else:
    num2 = int(input('Escriba un número: '))
    for i in range(num1-1):
        num3 = int(input('Escriba un número mas grande que {}: '.format(num2)))
        if num2 >= num3:
            print('¡{} no es mayor a {}!'.format(num3, num2))
        num2 = num3
print('Gracias por su colaboración') 