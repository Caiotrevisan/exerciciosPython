'''Implemente a função busca(lista, elemento), que busca
um determinado elemento em uma lista e devolve o índice
correspondente à posição do elemento encontrado. Utilize
o algoritmo de busca sequencial. Nos casos em que o
elemento buscado não existir na lista, a função deve
devolver o booleano False.'''


def busca(lista,elemento):
    for i in range(len(lista)):
        if elemento == lista[i]:
            return i
    return False

def test1():
    return busca(['a', 'e', 'i'], 'e')

def test2():
    return busca([12, 13, 14], 15)
