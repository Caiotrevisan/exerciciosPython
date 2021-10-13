def fatorial(n):
    resultado = 1
    while n > 1:
        resultado = resultado * n
        n = n - 1

    return(resultado)

n = int(input("Digite um número: "))
while n > 0:
    print(fatorial(n))
    n = int(input("Digite um número: "))

