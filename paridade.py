import math
numero = float(input('Digite um número:'))

sobra = numero % 2

if sobra == 0:
    print('Par')
else:
    print('Ímpar')