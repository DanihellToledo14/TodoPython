#Dados
import random

print('***JUEGO DE DADOS***')
dados = int(input('Ingrese cantidad de dados a lanzar: '))
if dados < 1:
    print('^Imposible^')
else:
    print('DADOS')
    for i in range(1,dados+1):
        print('Dado {}) '.format(i), random.randrange(1, 7))

