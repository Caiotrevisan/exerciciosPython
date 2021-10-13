def computador_escolhe_jogada(n,m):
    y = 1
    while (n-y)%(m+1) != 0 and y < m:
        y = y + 1
    print("O computador tirou",y,"peças.")
    return y
    
def usuario_escolhe_jogada(n,m):
    x = int(input("Quantas peças você vai tirar? "))

    while x > m and x < 0:
        print("Oops! Jogada inválida! Tente de novo.")
        x = int(input("Quantas peças você vai tirar? "))

    print("Você tirou", x,"peças.")
    return x

def partida():
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))

    while m <= 0 and n <= 0:
        print("Oops! Jogada inválida! Tente de novo.")
        n = int(input("Quantas peças? "))
        m = int(input("Limite de peças por jogada? "))
    
    if n%(m+1) > 0:
        print("Computador começa!")
        comp = True

    else:
        print("Você começa!")
        comp = False

    if comp == True:
        while n > 0:
            n = n - computador_escolhe_jogada(n,m)
            if n > 0:
                print("Agora restam",n,"peças no tabuleiro.")
                n = n - usuario_escolhe_jogada(n,m)
                if n > 1:
                    print("Agora restam", n,"peças no tabuleiro.")

                else:
                    print("Agora resta apenas uma peça no tabuleiro.")

        print("Fim de jogo! O computador ganhou!")

    else:
        while n > 0:
            n = n - usuario_escolhe_jogada(n,m)
            if n > 0:
                if n > 1:
                    print("Agora restam", n,"peças no tabuleiro.")

                else:
                    print("Agora resta apenas uma peça no tabuleiro.")

            n = n - computador_escolhe_jogada(n,m)

            if n > 0:
                print("Agora restam", n, "peças no tabuleiro.")

            else:
                print("Fim de jogo! O computador ganhou!")

        
            

def campeonato():
    print("Você escolheu campeonato!")
    print("**** Rodada 1 ****")
    partida()
    print("**** Rodada 2 ****")
    partida()
    print("**** Rodada 3 ****")
    partida()

    print("**** Final do campeonato! ****")
    print("Placar: Você 0 x 3 Computador")

print("Bem-vindo ao jogo do NIM! Escolha:")

print("1 - para jogar uma partida isolada")
print("2 - para jogar um campeonato")

tipo = int(input())

if tipo == 1:
    print("Você escolheu uma partida!")
    partida()

else:
    campeonato()
