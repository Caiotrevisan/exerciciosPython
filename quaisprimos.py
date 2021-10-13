def eprimo(a):
    primo = True
    x = 2

    while primo == True and x < a:
        if (a/x)%1 != 0:
            primo = True
            x = x+1

        else:
            primo = False

    return primo


limite = int(input("Limite máximo: "))

n = 2
while n < limite:
    if eprimo(n):
        print(n, end=", ")
    n = n + 1
