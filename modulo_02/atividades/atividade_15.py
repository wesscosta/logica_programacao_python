"""
Cadastre cinco produtos e suas respectivas quantidades em estoque.

Ao final, apresente uma mensagem informando quais produtos possuem quantidade igual ou inferior a cinco unidades.
"""
produtos=[]
quantidades=[]

for i in range(5):
    produto=input("Digite o nome do produto: ")
    quantidade=int(input("Digite a quantidade de produto em estoque: "))
    
    produtos.append(produto)
    quantidades.append(quantidade)
    
print("\nprodutos em estoque igual ou inferior a cinco:")

for i in range(len(produtos)):
    if quantidades[i] <= 5:
        print(f"produto {produtos[i]} com {quantidades[i]} unidades")
    
    


