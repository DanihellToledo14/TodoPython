print('Ejercicio 18: Numero mas cercano.')
print()

#Solicitud de datos
num1  = int(input('    Ingrese el Primer  numero: '))#10
num2 = int(input('    Ingrese el Segundo numero: '))#7
num3  = int(input('    Ingrese el Tercer  numero: '))#3
num4  = int(input('    Ingrese el Cuarto  numero: '))#12
num5  = int(input('    Ingrese el Quinto  numero: '))#15

# Se realizan las restas para hallar la menor diferencia.
#--------------------------------
Resta1 = num1 - (num2)# 10-7 = 3 
Resta2 = num1 - (num3)# 10-3 = 7
Resta3 = num1 - (num4)# 10-12= -2
Resta4 = num1 - (num5)# 10-15= -5
#--------------------------------
menor_dif = Resta1 
#--------------------------------
if Resta2 < menor_dif and Resta2 >= 0:
    menor_dif = Resta2 
else:
                            if Resta2 > menor_dif and Resta2 <= 0:
                                menor_dif = Resta2

#--------------------------------
if Resta3 < menor_dif and Resta3 >= 0:
    menor_dif = Resta3
else:
                            if Resta3 > menor_dif and Resta3 <= 0:
                                menor_dif = Resta3
                
#--------------------------------
if Resta4 < menor_dif and Resta4 >= 0:
    menor_dif = Resta4
else:
                            if Resta4 > menor_dif and Resta4 <= 0:
                                menor_dif = Resta4

#--------------------------------
num_cer = num1 - menor_dif
#--------------------------------
print('    El numero mas cercano a %d es %d.'%(num1,num_cer))