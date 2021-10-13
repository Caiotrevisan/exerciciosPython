def delta(a,b,c):
    import math

    delta = b**2 - 4*a*c

    return delta



def bhaskara(a,b,c):

    if delta(a,b,c) >= 0:
        x1 = (-b + math.sqrt(delta(a,b,c)))/2*a
        x2 = (-b - math.sqrt(delta(a,b,c)))/2*a

        if delta(a,b,c) > 0:
            resposta = x1, x2

        else:
            resposta = x1

    else:
        resposta = "não possui raizes reais"
        
    return resposta



