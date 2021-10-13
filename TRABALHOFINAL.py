import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def compara_assinatura(as_a, as_b):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''


    

def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''

    #1 Tamanho médio de palavra é a soma dos tamanhos das palavras dividida pelo número total de palavras.
    somaTamanho = 0
    palavrasSeparadas = separa_palavras(texto)
    for i in palavrasSeparadas:
        somaTamanho += len(i)
    
    totalpalavras = len(separa_palavras(texto))
    mediapalavra = somaTamanho/totalpalavras

    #2 Relação Type-Token é o número de palavras diferentes dividido pelo número total de palavras.
    palavrasDiferentes = []
    for i in palavrasSeparadas:
        if i not in palavrasDiferentes:
            palavrasDiferentes.append(i)

    TypeToken = len(palavrasDiferentes)/totalpalavras

    #3 Razão Hapax Legomana é o número de palavras que aparecem uma única vez dividido pelo total de palavras
    palavrasUnicas = []
    palavrasRepetidas = palavrasSeparadas[:]
    
    for i in palavrasDiferentes:
        if i in palavrasRepetidas:
            palavrasRepetidas.remove(i)
    
    for i in palavrasDiferentes:
        if i not in palavrasRepetidas:
            palavrasUnicas.append(i)

    Hapax = len(palavrasUnicas)/totalpalavras

    #4 Tamanho médio de sentença é a soma dos números de caracteres em todas as sentenças dividida pelo número de sentenças

    sentencas = separa_sentencas(texto)
    somaCaracteres = 0
    palavras = []
    for i in texto:
        if i != " " and i != "," and i != "." and i != "!" and i != "?":
            palavras.append(i)
    
    for i in palavras:
       somaCaracteres += len(i)


    mediaSentencas = somaCaracteres/len(sentencas)


    #5 Complexidade de sentença é o número total de frases divido pelo número de sentenças.
    
    totalFrases = len(separa_frases(texto))
    totalSentencas = len(sentencas)

    Complexidade = totalFrases/totalSentencas


    #6 Tamanho médio de frase é a soma do número de caracteres em cada frase dividida pelo número de frases no texto.

    Frases = separa_frases(texto)
    numeroFrases = len(Frases)

    mediaFrases = somaCaracteres/numeroFrases


    return [mediapalavra, TypeToken, Hapax, mediaSentencas, Complexidade, mediaFrases]
        

def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    
    # dividir os elementos da lista pelo infectado, qual der mais proximo de 1
    assinaturas = []
    
    for i in textos:
        ass_i = calcula_assinatura(i)
        assinaturas.append(ass_i)
        

    provaveis = assinaturas[:ass_cp]
    maisProvavel = provaveis[-1]
    
    return 
        


def main():
    ass_cp = le_assinatura()

    textos = le_textos()

    avalia_textos(textos,ass_cp)

    








    
