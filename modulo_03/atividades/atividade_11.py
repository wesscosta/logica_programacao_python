# Solicite ao usuário o nome, o preço e a quantidade em estoque de um produto e armazene essas informações em um dicionário. Em seguida, adicione a categoria, atualize o preço, aumente a quantidade em estoque e, ao final, apresente todos os dados atualizados.

nome = input("Digite o nome:")
email = input("Digite o e-mail:")
cidade = input("Digite a cidade:")

pessoa = {
    "nome": nome,
    "email": email,
    "cidade": cidade
}
chave = input("Digite a informação que deseja consultar:")

resultado = pessoa.get(chave)

if resultado is None:
    print("Dado não encontrado.")
else:
    print("Dado encontrado:",resultado)
