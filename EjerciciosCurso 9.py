#Ejercicio 9: Radar de velocidad.
# Valores para Dibujar la Tabla.
ANCHO = 40
R1 = "-"
R2 = " "
VACIO = ""

# Mensajes a Mostrar.
Msj_Inic = "RADAR DE VELOCIDAD"

# Declaracion de variables.
Vel = 0.0
f0 = 2e-10            
f1 = 2.0000004e-10    

# Formato de Salida Final en Pantalla.
Resp = ">>> La Velocidad es: %0.2f millas/hora."

# Encabezado del Programa.
# LINEA 1: Parte superior de la Tabla.
print(VACIO.center(ANCHO,R1))
# Mensaje Centrado.
print(Msj_Inic.center(ANCHO,R2))

# Inicio del Programa:
# Calculo de la VELOCIDAD del radar
# velocidad = 6.685x10^8 x (f1 - f0) / (f1 + f0)
Vel = 6.685e8*(f1-f0)/(f1+f0)

# LINEA 2: Separador de la tabla
print(VACIO.center(ANCHO,R1))
# Se muestra el mensaje en Pantalla
print(Resp.center(ANCHO,R2) %(Vel))

# LINEA 3: Parte Inferior de la Tabla
print(VACIO.center(ANCHO,R1))
