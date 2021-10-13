def é_hipotenusa(a):
    i = 1
    j = 1
    while a**2 != (i**2 + j**2) and j < a:
        while i < a and a**2 != (i**2 + j**2):
            i += 1
        if a**2 != (i**2 + j**2):
            i = 1
            j += 1
    
    
    if a**2 == (i**2 + j**2):
        return True
    else:
        return False

    

def soma_hipotenusas(n):
    h = 1
    soma = 0
    while h <= n:
        if é_hipotenusa(h):
            soma = soma + h
        h = h+1

    return soma
