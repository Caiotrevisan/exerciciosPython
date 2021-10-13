def fatorial(n):

	resultado = 1

	while n > 0:
	
		resultado = resultado * n
		n = n - 1
	
	return resultado

def numero_binomial(n,k):
        return fatorial(n)/(fatorial(k)*fatorial(n-k))





def teste_fatorial():
        if fatorial(0) == 1:
                print("funciona para 0")
        else:
                print("não funciona para 0")

        if fatorial(1) == 1:
                print("funciona para 1")
        else:
                print("não funciona para 1")

        if fatorial(2) == 2:
                print("funciona para 2")
        else:
                print("não funciona para 2")

        if fatorial(3) == 6:
                print("funciona para 3")
        else:
                print("não funciona para 3")

        if fatorial(4) == 24:
                print("funciona para 4")
        else:
                print("não funciona para 4") 
