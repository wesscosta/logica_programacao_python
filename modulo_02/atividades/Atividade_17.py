"""
Cadastre diversos produtos.

O cadastro deverá continuar até que o usuário digite **fim**.

Depois, solicite o nome de um produto e informe se ele está cadastrado.

Caso exista, informe sua posição na lista.
"""

produtos = []

while True:
    nome = input("Digite o nome do produto ou (fim) para encerrar: ")
    
    if nome.lower() == "fim":
        break
    
    produtos.append(nome)

verificacao = input("\nDigite o nome do produto que deseja verificar: ")

if verificacao in produtos:
    posicao = produtos.index(verificacao)
    print(f"PRODUTO NA POSIÇÃO: {posicao + 1}")
else:
    print("Produto não encontrado!")
