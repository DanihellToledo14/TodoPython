print('SUMA ENTRE VALORES')
suma = 0
num1 = int(input('Escriba un numero entero positivo: '))
if num1 < 0:
    print('¡Le he pedido un numero entero positivo!')
elif num1 == 0:
    print('¡Escriba un número mayor a 0!')
else:
    num2 = int(input('Escriba un numero entero positivo mayor que {}: '.format(num1)))
    if num2 < num1:
        print('¡Escriba un numero mayor que {}!'.format(num1))
    elif num1 == num2:
        print('¡Escriba un nunero mayor a {}!'.format(num1))
    else:
        for i in range(num1, num2 + 1):
            suma = suma + i
        print('La suma desde {} hasta {} es {}'.format(num1, num2, suma))
        for i in range(num1, num2):
            print('{} +'.format(i))
        print('{} = {}'.format(num2, suma))
            
            