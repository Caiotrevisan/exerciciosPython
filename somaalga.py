soma = 0
numero = int(input("Digite um número: "))
sobra = 0
x = 1

while x > 0:	
	x = numero//10
	sobra = numero % 10
	soma = soma + sobra
	numero = x

print(soma)

