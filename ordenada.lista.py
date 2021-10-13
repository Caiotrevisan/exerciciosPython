'''Escreva a função ordenada(lista), que recebe uma lista com números
inteiros como parâmetro e devolve o booleano True se a
lista estiver ordenada e False se a lista não estiver ordenada.'''

def ordenada(lista):
    lista2 = sorted(lista)
    if lista == lista2:
        return True
    else:
        return False

    
def test():
    lista = [2,4,1,5]
    return ordenada(lista)
