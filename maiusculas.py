def maiusculas(frase):
    maiusculas = ""
    for i in frase:
        if ord(i) < 91 and ord(i) > 64:
            maiusculas += i

    return maiusculas
            
