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
    i = 0
    modu = []
    while i < 6:
        modu.append(abs(as_a[i] - as_b[i]))
        i += 1

    simi = sum(modu)/len(modu)

    return simi
    
    

    

def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''

    #1 Tamanho médio de palavra é a soma dos tamanhos das palavras dividida pelo número total de palavras.
    texto = texto.lower()
    listadesentencas = separa_sentencas(texto)
    listadefrases = [] 
    for sentenca in listadesentencas:
        listadefrases.extend(separa_frases(sentenca))

    listadepalavras = []
    for frase in listadefrases:
        separa_palavras(frase)
        listadepalavras.extend(separa_palavras(frase))

    somaTamanho = 0    
    for i in listadepalavras:
        somaTamanho += len(i)
    
    totalpalavras = len(listadepalavras)
    mediapalavra = somaTamanho/totalpalavras

    #2 Relação Type-Token é o número de palavras diferentes dividido pelo número total de palavras.
    palavrasDiferentes = []
    for palavra in listadepalavras:
        if palavra not in palavrasDiferentes:
            palavrasDiferentes.append(palavra)


    TypeToken = len(palavrasDiferentes)/totalpalavras

    #3 Razão Hapax Legomana é o número de palavras que aparecem uma única vez dividido pelo total de palavras
    palavrasUnicas = []
    palavrasRepetidas = listadepalavras[:]
    
    for i in palavrasDiferentes:
        if i in palavrasRepetidas:
            palavrasRepetidas.remove(i)
    
    for i in palavrasDiferentes:
        if i not in palavrasRepetidas:
            palavrasUnicas.append(i)

    Hapax = len(palavrasUnicas)/totalpalavras

    #4 Tamanho médio de sentença é a soma dos números de caracteres em todas as sentenças dividida pelo número de sentenças
    somaCaracteres = 0
    
    for i in listadesentencas:
        somaCaracteres += len(i)


    mediaSentencas = somaCaracteres/len(listadesentencas)


    #5 Complexidade de sentença é o número total de frases divido pelo número de sentenças.
    totalFrases = len(listadefrases)
    totalSentencas = len(listadesentencas)

    Complexidade = totalFrases/totalSentencas


    #6 Tamanho médio de frase é a soma do número de caracteres em cada frase dividida pelo número de frases no texto.
    somaCaracteresfrase = 0
    for i in listadefrases:
        somaCaracteresfrase += len(i)
    
    mediaFrases = somaCaracteresfrase/len(listadefrases)


    return [mediapalavra, TypeToken, Hapax, mediaSentencas, Complexidade, mediaFrases]
        

def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''

    assinaturas = []
    similaridade = []
    for a in textos:
        assinaturas.append(calcula_assinatura(a))

    modulo = []
    i = 0
    for b in assinaturas:
        while i < 6:
            modulo.append(abs(b[i] - ass_cp[i]))
            i += 1
        similaridade.append(sum(modulo)/len(modulo))
        modulo = []
        i = 0   

    listacrescente = sorted(similaridade)
    assinatura = listacrescente[0]
    print(similaridade)
    print(assinatura)
    
        
    numerodotexto = similaridade.index(assinatura)
       
    
    return numerodotexto + 1
         
        
def main():
    ass_cp = le_assinatura()
    textos = le_textos()

    ntexto = avalia_textos(textos, ass_cp)

    as_a = calcula_assinatura(textos[ntexto])

    as_b = ass_cp
    
    a = compara_assinatura(as_a, as_b)
        
    print("O autor do texto",ntexto, "está infectado com COH-PIAH")


main()

