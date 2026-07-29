#Solicite um número inteiro ao usuário e apresente a contagem regressiva até zero.
valor = int(input("digite um numero inteiro: "))

for numero in range(valor,0,-1):
 print(numero)
