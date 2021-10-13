numero = float(input('Digite um número:'))

sobra = numero % 5
if sobra == 0:
    print('Buzz')
else:
    print(numero)