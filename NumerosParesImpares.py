#Numeros Pares e Impares:

num1 = int(input('Escriba un numero entero: '))
num2 = int(input('Escriba otro numero entero mayor o igual que {} : '.format(num1)))
if num1 > num2:
    print('¡Le he pedido un numero mayor o igual que {}! '.format(num1))
else:
    for i in range(num1, num2 + 1):
        if i%2 == 0:
            print('{} es par'.format(i))
        else:
            print('{} es impar'.format(i))
            