"""
Desenvolva um programa que permita cadastrar dez produtos. Ao final, apresente todos os produtos cadastrados em ordem alfabética.
"""
produtos = []

for produto in range(10):
    produto = input("digite o produto para cadastrar: ")
    produtos.append(produto)
    produtos.sort()

for produto in produtos:
    print(f"{produto}")


