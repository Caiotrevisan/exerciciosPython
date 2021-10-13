print("digite uma sequência de números terminada por zero.")
soma = 0

valor = 1

while valor != 0:
	valor = int(input("Digite um número: "))
	soma = soma + valor
print("A soma é: ", soma)