print('CONTADOR DE PARES E IMPARES')
j = 0
k = 0
num1 = int(input('¿Cúantos valores va a introducir?: '))
if num1 < 0:
    print('¡Imposible!')
elif num1 == 0:
    print('El valor ingresado no corresponde.')
else:
    for i in range(1, num1+1):
        numero = int(input('Escriba el {}) número: '.format(i)))
        if numero % 2== 0:
            j = j + 1
        else:
            k = k +1
print('Ha escrito {} números pares y ha escrito {} números impares'.format(j, k))
print('¡Gracias por su colavoración!')
     
            