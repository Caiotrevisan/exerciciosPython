tamanho = int(input("digite o tamanho da sequência: "))
produto = 1

i = 0
valor = 1
while i < tamanho:
	valor = int(input("Digite um número: "))
	produto = produto * valor
	i = i + 1
print("O produto é:", produto)