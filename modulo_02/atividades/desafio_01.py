#Desenvolva um programa que simule um saque bancário. Solicite o saldo disponível e o valor desejado para saque. Caso o valor seja menor ou igual ao saldo, informe que a operação foi realizada com sucesso e apresente o novo saldo. Caso contrário, exiba uma mensagem informando saldo insuficiente. Considere também valores inválidos, como saque igual ou menor que zero.

saldo = 1537.90
print (f"seu saldo é de: {saldo}")
saque = float (input ("digite o valor do saque: " ))
if saldo >= saque:
    print ("saque aprovado")
    saldo = saldo-saque
    print( f"seu saldo atual é: {saldo}")
elif  saldo < saque:
    print ("saque negado")

