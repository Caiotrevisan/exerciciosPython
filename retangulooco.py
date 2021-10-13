largura = int(input("Digite a largura: "))
altura = int(input("Digite a altura: "))
x = 1
y = 1

while x <= altura:
    while y <= largura:
        if y > 1 and y < largura and x > 1 and x <altura:
            print(" ",end = "")
        else:
            print("#", end = "")
        y = y+1
    x = x + 1
    print()
    y = 1
