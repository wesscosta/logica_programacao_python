#Solicite ao usuário o título, o autor, o ano e a categoria de um livro e armazene essas informações em um dicionário. Em seguida, apresente todas as chaves utilizando keys(), todos os valores utilizando values() e todos os pares chave-valor utilizando items(). Depois, percorra o dicionário com for e items() para apresentar todas as informações cadastradas.

titulo = input("Digite o titulo do livro: ")
autor = input("Digite o nome do autor: ")
ano = int(input("Digite o ano do livro: "))
categoria = input("Digite a categoria do livro: ")

livro = {
    "titulo" : titulo,
    "autor" : autor,
    "ano" : ano,
    "categoria" : categoria
}

print(f"\nTodas as chaves {livro.keys()}")
print(f"\nTodos os valores {livro.values()}")

for chave , valor in livro.items():
     print(f"{chave}: {valor}")
       