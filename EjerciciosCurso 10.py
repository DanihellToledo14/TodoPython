#Ejercicio 10: Calculadora freelancer
# Valores para Dibujar la Tabla.
ANCHO = 40
R1 = "-"
R2 = " "
VACIO = ""

# Mensajes a Mostrar.
Msj_Inic = "CALCULADORA FREELANCER (USD)"
Msj_dolar = '>>>Precio en dolares por hora: 20'
Msj_Resp = ">>>PAGO SEMANAL: %4.2f \n>>>PAGO MENSUAL: %4.2f"

# Declaracion de variables.
dolares = 20.0
pagoSEM = 0.0
pagoMEN = 0.0

# Encabezado del Programa.
# LINEA 1: Parte superior de la Tabla.
print(VACIO.center(ANCHO,R1))

# Mensaje Centrado.
print(Msj_Inic.center(ANCHO,R2))

# LINEA 2: Separador de la tabla.
print(VACIO.center(ANCHO,R1))

# Se muestra el mensaje en pantalla.
print(Msj_dolar)

#Inicio del programa.
#Calculo semanal y mensual.
#pagoSEM = dolares/h * 40
#pagoMEN = dolares/h * 160
pagoSEM = dolares * 40
pagoMEN = dolares * 160

#LINEA 3: Separador de la tabla.
print(VACIO.center(ANCHO,R1))

# Se muestra el mensaje en pantalla.
print(Msj_Resp%(pagoSEM, pagoMEN))

# LINEA 4: Parte Inferior de la Tabla
print(VACIO.center(ANCHO,R1))