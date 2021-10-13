def sao_multiplicaveis(m1,m2):
    if len(m1[0]) == len(m2):
        return True
    else:
        return False


def teste1():
    m1 = [[1, 2, 3], [4, 5, 6]]
    m2 = [[2, 3, 4], [5, 6, 7]]
    return sao_multiplicaveis(m1,m2)

def teste2():
    m1 = [[1], [2], [3]]
    m2 = [[1, 2, 3]]
    return sao_multiplicaveis(m1,m2)
