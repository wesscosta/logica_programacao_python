#Desenvolva um programa que solicite a idade do usuário e informe se ele pode acessar uma área restrita. O acesso somente deverá ser permitido para pessoas com 18 anos ou mais.
idade = int(input("Digite sua idade: "))

if (idade >= 18):
    print ("Acesso Liberado!")
else:
    print ("Acesso Negado!")
