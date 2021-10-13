def eprimo(numero):
    
    primo = True
    x = 2

    while primo == True and x < numero:
        if (numero/x)%1 != 0:
            primo = True
            x = x+1

        else:
            primo = False

    return primo

def maiorprimo(y):
    while eprimo(y) == False: 
        y = y - 1
        
    
    return y
