# Solicite ao usuário o nome, o preço e a quantidade em estoque de um produto e armazene essas informações em um dicionário. 
# Em seguida, adicione a categoria, atualize o preço, aumente a quantidade em estoque e, ao final, apresente todos os dados atualizados.

produto = {}

produto['Nome'] = input('Informe o nome do produto: ')
produto['Preco'] = float(input('Informe o preço do produto: '))
produto['Quantidade'] = int(input('Informe a quantidade do produto: '))

print(produto)

produto['Categoria'] = input('Informe a categoria do produto: ')
produto['Preco'] = float(input('Informe o preço atualizado: '))
produto['Quantidade'] = int(input('Informe a quantidade atualizada do produto: '))

print(produto)
