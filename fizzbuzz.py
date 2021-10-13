numero = float(input('Digite um número:'))

sobra5 = numero % 5
sobra3 = numero % 3

if sobra5 == 0 and sobra3 ==0:
    print('FizzBuzz')
else:
    print(numero)