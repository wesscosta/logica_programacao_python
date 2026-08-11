funcionario = {}

funcionario["Nome"] = input("Digite o nome do funcionário: ")
funcionario["Cargo"] = input("Digite o cargo do funcionário: ")
funcionario["Setor"] = input("Digite o setor do funcionário: ")
funcionario["Salário"] = input("Digite o salário do funcionário: ")

for chave, valor in funcionario.items():
    print(f'{chave} : {valor}')

chave_remove = input("Digite a chave que quer remover: ")

if chave_remove in funcionario:
    removido = funcionario.pop(chave_remove)
    for chave, valor in funcionario.items():
        print(f'{chave} : {valor}')

    
else:
    print("Chave não cadastrada")
