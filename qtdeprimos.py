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

def n_primos(a):

    total = 0
    b = 2

    while b <= a:    
        if eprimo(b):
            total = total + 1
            b = b + 1
        else:
            b = b + 1

    return total
