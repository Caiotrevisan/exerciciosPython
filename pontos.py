import math
x1 = float(input('Digite o número x1:'))
x2 = float(input('Digite o número x2:'))
y1 = float(input('Digite o número y1:'))
y2 = float(input('Digite o número y2:'))

distancia = math.sqrt((x1 - x2)**2 + (y1-y2)**2)

if distancia > 10:
    print('longe')
else:
    print('perto')