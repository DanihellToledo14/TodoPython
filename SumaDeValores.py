suma = 0
num1 = int(input('¿Cúantos valores va a introducir?: '))
if num1 < 0:
    print('¡Imposible!')
elif num1 == 0:
    print('Escriba un número mayor a 0')
else:
    for i in range(1, num1+1):
        numero = float(input('Escriba el {}) número: '.format(i)))
        suma = suma + numero
print('La suma de los numeros que ha escrito es: {}'.format(suma))