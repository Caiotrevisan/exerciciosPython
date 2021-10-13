def primeiro_lex(lista):
    menor = lista[0]
    for i in lista:
        i = str(i)
        b = 0
        if ord(i[b]) <= ord(menor[b]):
            while i[b] == menor[b] and b < (len(i)-1) and b < (len(menor)-1):
                b += 1
            menor = i
     
    return menor
        
