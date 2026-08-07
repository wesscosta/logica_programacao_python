"""Desenvolva um programa que simule o cadastro simplificado de livros de uma biblioteca.

O sistema deverá apresentar um menu com as seguintes opções:

```
1 - Cadastrar livro
2 - Listar livros
3 - Pesquisar livro
4 - Remover livro
5 - Encerrar
```

Os livros deverão ser armazenados em uma lista durante toda a execução do programa.

Ao pesquisar ou remover um livro inexistente, o sistema deverá informar o usuário.
"""


livros=[]

while True:
    print ("""
    1 - Cadastrar livro
    2 - Listar livros
    3 - Pesquisar livro
    4 - Remover livro
    5 - Encerrar
    """
    )

    opcao = input('digite uma opção: ')
    
    # validar se o valor é decimal antes de converter
    if opcao.isdecimal() == True: 
        opcao = int(opcao)
    else:
        print("Digite um valor numerico: ")
        continue
        
    
    match opcao:
        case 1:
            livro_cadastrado = input('digite livro para cadastro: ')
            livros.append(livro_cadastrado)
        case 2:
            print(livros)
        case 3:
            livro_pesquisar = input("digite livro para pesquisar: ")
            if livro_pesquisar in livros:
                print('livro encontrado')
            else:
                print('livro nao encontrado')
        case 4:
            livro_remover = input("digite livro para Remover: ")
            if livro_remover in livros:
                livros.remove(livro_remover)
                print('livro removido')
            else:
                print('livro nao esta na lista')
        case 5:
            print('programa encerrado.')
            break
        case _:
            print('opção invalida')

# Outra opção seria apenas trabalhar a opção escolhida como str e as opções do match-case como str também " "
