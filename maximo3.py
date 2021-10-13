def maximo(a,b,c):

    maximo = 0


    if a >= b and a >= c:
        maior = a
      
    else:
        if b >= a and b >= c:
            maior = b

        else:
            maior = c

    return(maior)
