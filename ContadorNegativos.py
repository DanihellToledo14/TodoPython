print('NUMEROS NEGATIVOS')
j = 0
num1 = int(input('¿Cúantos valores va a introducir?: '))
if num1 < 0:
    print('¡Imposible!')
elif num1 == 0:
    print('No has escrito ningún número negativo')
else:
    for i in range(1, num1+1):
        numero = int(input('Escriba el {}) número: '.format(i)))
        if numero < 0:
            j = j + 1
    print('Ha escrito {} números negativos'.format(j))