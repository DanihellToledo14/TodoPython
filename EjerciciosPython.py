#Promedio
print('MAYOR, MENOR Y MEDIA ARITMETICA')

num1 = int(input('¿Cúantos valores va a introducir?: '))

media = 0
mayor = 0

if num1 <= 0:
   print('¡Imposible!')
else:
   menor = int(input('Escriba el 1) numero: '))
   
   media += menor
   
   for i in range(2,num1 + 1):
        
        num2 =  int(input('Escriba el {}) numero: '.format(i)))
        
        if num2 > mayor:
            mayor = num2
        elif num2 < menor:
            menor = num2
            
        media += num2
                
   print('El numero mas chico es {}'.format(menor))
   print('El número mas grande es {}'.format(mayor))
   print('La media de los numeros es {}'.format(media/num1))
   
   
   
   
   