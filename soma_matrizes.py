def dimensoes(minha_matriz):
    a = len(minha_matriz)

    b = len(minha_matriz[0])


    return str(a) + "X" + str(b)



def soma_matrizes(m1,m2):
    matrizfinal = []
    matrizz = []
    i = 0
    j = 0
    
    if dimensoes(m1) == dimensoes(m2):
        while i < len(m1):
            while j < len(m1[0]) :
                matrizfinal.append((m1[i][j]) + (m2[i][j]))
                j += 1
            i += 1
            j = 0
            matrizz.append(matrizfinal)
            matrizfinal = []

        return matrizz

    else:
        return False
        

def teste():
    print(soma_matrizes([[1, 2, 3], [4, 5, 6]],[[2, 3, 4], [5, 6, 7]]))

