#Blucle for: Con 2 argumentos. Inicio y final del rango. El rango siempre llega hasta el n-1, en este caso hasta 10 = (11-1).

for i in range (1, 11):
    if i <= 5:
        print(i)
    else:
        print ('Los numeros son mayores')
        
#Blucle for: Con 3 argumentos. Inicio, Final y paso. Comienza en 1 hasta 10 y va recorriendo de a 2 elementos.
        
for i in range(1, 11, 2):
    print(i)
    
#Blucle for: Con argumentos negativos. 
    
for i in range(-10, 0):
    print(i)