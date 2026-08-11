#Desenvolva um programa para gerenciar o cadastro de um livro. Solicite ao usuário o título, o autor, o ano, a quantidade de páginas e a disponibilidade e armazene essas informações em um dicionário.
#O programa deverá apresentar um menu que permita consultar uma informação, alterar um valor, adicionar uma nova informação, remover uma informação, visualizar todo o cadastro e encerrar o programa.Durante as operações, verifique a existência das chaves quando necessário e utilize os recursos estudados, como `get()`, `in`, `not in`, `items()`, `update()` e `pop()`, juntamente com estruturas condicionais e de repetição.
#O programa deverá permanecer em execução até que o usuário escolha a opção de sair.

cadastro_livro = {}

cadastro_livro["titulo"] = input("Informe o titulo do livro: ")
cadastro_livro["autor"] = input("Informe o autor do livro: ")
cadastro_livro["ano"] = input("Informe o ano do livro: ")
cadastro_livro["quantidade"] = input("Informe a quantidade de páginas do livro: ")
cadastro_livro["disponibilidade"] = input("Informe se o livro está 'disponivel' ou 'indisponivel': ")

print("\n=== MENU DE OPÇÕES ===")
print("1 - Consultar uma informação")
print("2 - Alterar um valor")
print("3 - Adicionar uma nova informação ")
print("4 - Remover uma informação")
print("5 - Visualizar todo cadastro")
print("6 - Encerrar programa")

while True:
    opcao = int(input("Digite a opção desejada : "))
    if opcao == 6:
        print("Programa encerrado!")
    match opcao:

        case 1:
            informacao = input("Qual informação voce deseja consultar: ")
            resultado = cadastro_livro.get(informacao, "Informação não encontrada!")
            print(resultado)

        case 2:
            alterar = input("Informe o valor que deseja alterar: ")
            alteracao = input(f"Qual o novo valor de {alterar}")
            
            cadastro_livro['alterar'] = alteracao
            print(cadastro_livro)
        
        case 3:
            adicionar = input("Digite a nova informação: ")    
            informacao = input("Digite o valor da informação: ")
            cadastro_livro.update({adicionar : informacao})         
                
        case 4:
            remover = input("Digite a informação que deseja remover: ")
            if remover in cadastro_livro:
                del cadastro_livro[remover]

        case 5:
            print(cadastro_livro)
        
        case _:
            print("Opção inválida!")
