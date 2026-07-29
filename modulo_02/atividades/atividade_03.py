# Solicite o nome, peso e altura do usuário. Calcule o IMC e informe a classificação utilizando estruturas condicionais.Utilize a tabela oficial da OMS para definir as faixas.
nome = input ('nome do usuario')
altura = float(input('altura'))
peso = float(input('peso'))

imc = peso / (altura*altura)

if imc <= 18.5: print("Baixo peso (magreza)")
elif imc <= 24.9: print('Peso normal')
elif imc <= 29.9: print('Sobrepeso')
elif imc <= 34.9: print("Obesidade grau I")
elif imv <= 39.9: print('Obesidade grau II')
elif imc >=  40: print("Obesidade grau III (mórbida)")
