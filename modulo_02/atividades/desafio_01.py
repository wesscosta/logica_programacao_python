#Desenvolva um programa que simule um saque bancário. Solicite o saldo disponível e o valor desejado para saque. Caso o valor seja menor ou igual ao saldo, informe que a operação foi realizada com sucesso e apresente o novo saldo. Caso contrário, exiba uma mensagem informando saldo insuficiente. Considere também valores inválidos, como saque igual ou menor que zero.

saldo = float(input("Digite seu saldo: (R$)"))
saque = float (input ("Digite o valor do saque (R$): " ))

if saque <= 0:
    print("Valor invalido")
else:
    if saldo >= saque:
        print ("Saque aprovado")
        saldo = saldo-saque
        print( f"Seu saldo atual é: {saldo}")
    elif  saldo < saque:
        print ("Saque negado")

