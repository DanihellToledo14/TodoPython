print('MAYOR, MENOR Y MEDIA ARITMETICA')

mayor = 0
menor = 0
num1 = int(input('¿Cúantos valores va a introducir?: '))

if num1 < 0:
    print('¡Imposible!. Solo numeros positivos')
else:
    for i in range(1, num1+1):
        menor = int(input('Escriba el {}) numero: '.format(i)))
        if mayor < menor:
            mayor = menor
        elif mayor > menor:
            menor = mayor
        else:
            print()
    
   
        