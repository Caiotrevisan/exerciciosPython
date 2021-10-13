def eprimo(a):
    primo = True
    x = 2

    while primo == True and x < a/2:
        if (a/x)%1 != 0:
            primo = True
            x = x+1

        else:
            primo = False

    return primo

n = int(input("Digite um número inteiro:"))

while n > 0:
    if eprimo(n):
        print(n, "é primo!")
    else:
        print(n,"não é primo =[")

    n = int(input("Digite um número inteiro:"))
