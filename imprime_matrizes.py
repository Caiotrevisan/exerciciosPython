def imprime_matriz(m):
    for i in m:
        for a in i:
            if i.index(a) != len(i) - 1:
                print(a,end=" ")
            else:
                print(a)

def teste():
    return imprime_matriz([[1, 2, 3], [4, 5, 6]])
