nome_produto = "Caneca de café"
quantidade_estoque = 50
preco = 14.9
disponivel = True
desconto = None

print(f"Nome: {nome_produto}", type(nome_produto))
print(f"Quantidade {quantidade_estoque}", type(quantidade_estoque))
print(f"Preço: {preco}", type(preco))
print(f"Disponivel: {disponivel}", type(disponivel))
print(f"Desconto: {desconto}", type(desconto))

desconto = 10.0
print(f"\nDesconto: {desconto}", type(desconto))
#o tipo da variavel mudou porque o python permite reatribuição de valores
#por conta de sua tipagem dinamica e flexivel
