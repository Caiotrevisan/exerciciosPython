'''recebe uma lista de strings contendo nomes de pessoas como parâmetro e devolve o nome mais curto,
o nome mais curto que tiver dentro dessa lista de strings. A função deve ignorar espaços antes e depois do nome e
deve devolver o nome, entre aspas, capitalizado, ou seja, apenas com a primeira letra maiúscula.'''

def menor_nome(a):
    menorNome = a[1]
    for i in a:
        i = str(i)
        if i < menorNome:
            menorNome = i

    return menorNome.capitalize().strip()
        
def teste():
    lista = ["lucas ","pedro","paulo","caio    ","natalia"]

    return menor_nome(lista)
