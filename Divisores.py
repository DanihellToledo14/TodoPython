#Divisores
print('Buscador de divisores.')
num1 = int(input('Escribe un numero mayor a 0: '))
if num1 < 0:
    print('¡Escribe un numero mayor a 0!')
else: 
    for i in range(1, num1+1):
        if num1 % i == 0:
            print('{} es divisor de {}'.format(num1, i))