n = 1
lista = []
while n != 0:
    lista.append(n)
    n = int(input("digite uma sequência de números terminada por 0: "))
    
y = len(lista)
x = 1

while x < y:
    print(lista[-x])
    x = x + 1
