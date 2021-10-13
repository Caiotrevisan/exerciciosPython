numero = int(input("Digite um número inteiro: "))
primo = True
x = 2

while primo == True and x < numero:
	if (numero/x)%1 != 0:
		primo = True
		x = x+1
	else:	
		primo = False

if primo == True:
	print("primo")
else:
	print("não primo")
		
		