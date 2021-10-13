largura = int(input("Digite a largura: "))
altura = int(input("Digite a altura: "))
x = 1
y = 1

while x <= altura:
    while y <= largura:
        print("#", end = "")
        y = y+1
    x = x + 1
    print()
    y = 1
