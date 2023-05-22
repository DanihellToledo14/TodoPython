#Ejercicio 21: Tabla de multiplicar.
print(">>>TABLA DE MULTIPLICAR")

#Solución 1: Bucle While
# Declaracion de variables
i = 0
resp = 0
num1 = 0

# Solicitud de Datos
num1 = int(input('>>> Introduce el numero a multiplicar: '))

while i >= 0 and i < 13:
    resp = num1 * i
    print("    %d x %2d = %d" %(num1, i,resp))
    i += 1

print()
#Solución 2: Bucle for in range.
# Solicitud de Datos:
num1 = int(input('>>> Introduce el numero a multiplicar: '))

for i in range(13):
    resp = num1 * i
    print("    %d x %2d = %d" % (num1,i,resp))
    
    