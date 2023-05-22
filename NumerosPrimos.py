#Numeros Primos
j = 0 #Variable que toma la cantidad de divisores.
num1 = int(input('Escribe un numero mayor a 1 : '))
if num1 < 1:
    print('¡Escribe un numero mayor a 1!')
else: 
    for i in range(1, num1+1):
        if num1 % i == 0:
            j = j + 1
    if j > 2:
        print('----{} No es primo.'.format(num1))
    else:
        print('----{} Es primo.'.format(num1))