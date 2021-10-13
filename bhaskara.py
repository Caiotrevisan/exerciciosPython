import math
a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))

delta = b**2 - 4*a*c

if delta >= 0:
    x1 = (-b + math.sqrt(delta))/2*a
    x2 = (-b - math.sqrt(delta))/2*a
    if delta > 0:  
        print('As raízes são:',x1,'e', x2)
    else:
        print('A única raiz é:',x1)
    
else:
    print('Não possui raizes reais')
    