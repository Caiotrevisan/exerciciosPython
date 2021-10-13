def computador_escolhe_jogada(n,m):
    y = m
    while (n-y)%(m+1) != 0 and y:
        y = y-1

    n = n - y
    print("O computador tirou",y,"peças.")

    if n == 0:
        print("Fim de jogo! O computador ganhou!")

    else:
        print("Agora restam", n,"peças.")
        usuario_escolhe_jogada(n,m)
    
def usuario_escolhe_jogada(n,m):
    x = int(input("Quantas peças você vai tirar? "))
    if x <= m and x > 0:
        n = n - x
        print("Você tirou", x,"peças.")
        print("restam", n, "peças")
        computador_escolhe_jogada(n,m)

    else:
        print("Oops! Jogada inválida! Tente de novo.")
        usuario_escolhe_jogada(n,m)

def partida():

        n = int(input("Quantas peças? "))
        m = int(input("Limite de peças por jogada? "))

        if n%(m+1) > 0:
            print("Computador começa!")
            computador_escolhe_jogada(n,m)

        else:
            print("Você começa!")
            usuario_escolhe_jogada(n,m)

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

