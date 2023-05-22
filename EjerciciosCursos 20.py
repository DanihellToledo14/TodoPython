#Ejercicio 20: ECUACION DE SEGUNDO GRADO.
# Importacion de librerias
from math import sqrt

#---------------------------------------------------------------------

# Valores para Dibujar la Tabla
ANCHO = 55
R1 = "-"
R2 = " "
VACIO = ""

#---------------------------------------------------------------------

Msj_Inic = "ECUACION DE SEGUNDO GRADO: ax^2 + bx + c = 0"

#---------------------------------------------------------------------

# Declaracion de Variables
a, b, c = 0, 0, 0
x1, x2  = 0.0, 0.0
disc = 0

#---------------------------------------------------------------------

# Encabezado del Programa
print(VACIO.center(ANCHO,R1))
print(Msj_Inic.center(ANCHO,R2))
print(VACIO.center(ANCHO,R1))

#---------------------------------------------------------------------

# Solicitud de Datos 
a = float(input(">>> Valor de a: "))
b = float(input(">>> Valor de b: "))
c = float(input(">>> Valor de c: "))

disc = b**2 - 4*a*c

try:
    x1 = (-b + sqrt(disc)) / (2 * a)
    x2 = (-b - sqrt(disc)) / (2 * a)

    print(VACIO.center(ANCHO,R1))

    if x1 == x2:
        print(">>> SOLUCION: x = %4.2f" % x1)
    else:
        print(">>> SOLUCIONES: x1 = %4.2f y x2 = %4.2f" % (x1, x2))

except ZeroDivisionError:

    print(VACIO.center(ANCHO,R1))

    if b != 0:
        print("La ecuacion no tiene solucion.")
    else:
        print("La ecuacion tiene infinitas soluciones.")

except ValueError:
    # Casos:
    # 1) Se produce una division por cero.
    # 2) Se produce por calcular la raız cuadrada de un discriminante negativo.
    print(VACIO.center(ANCHO,R1))
    print("No hay soluciones reales")

#---------------------------------------------------------------------

print(CADENA_VACIA.center(ANCHO,RELLENO1))