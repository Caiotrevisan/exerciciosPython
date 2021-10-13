numero = int(input("Digite um número: "))
x = 0
y = 1

while x != y and numero > 10:
	x = numero % 10
	y = (numero//10)%10
	numero = numero//10

if x == y:
	print("sim")
else:
	print("não")