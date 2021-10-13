qtde = int(input())
if qtde < 1:
    print("NÃO HOUVE PROCESSAMENTO")
    qtde = 1
    
somaMedia = 0    
i = 1

while qtde >= i:
    media = float(input())
    if media >= 6:
        print("PARABÉNS VOCÊ ESTÁ APROVADO")
    somaMedia += media
    i += 1


mediaGeral = somaMedia/qtde
print(mediaGeral)
