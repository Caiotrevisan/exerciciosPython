def bubble_sort(lista):
    trocou = True

    if len(lista) <= 1:
        return lista
    
    fim = len(lista) - 1
    while trocou == True:
        for i in range(fim):
            if lista[i] > lista[i+1]:
                lista[i], lista[i+1] = lista[i+1], lista[i]
                trocou = True
                print(lista)
            else:
                trocou = False
    return lista

