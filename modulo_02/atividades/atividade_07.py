#Solicite um número inteiro e apresente sua tabuada de 1 até 10 utilizando um laço de repetição.
numero = int(input("Digite um número inteiro"))

for i in range(1,11):
    print(f"{numero} * {i} = {numero*i}")
