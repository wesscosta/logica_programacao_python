"""
Solicite ao usuário o nome, a idade, a cidade e a profissão de uma pessoa. Armazene essas informações em um dicionário e, ao final, apresente cada dado utilizando sua respectiva chave.
"""
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
cidade = input("Qual sua cidade: ")
profissao = input("Qual a sua profissão: ")

pessoa = {
    "nome": nome,
    "idade": idade,
    "cidade": cidade,
    "profissão": profissao
}

print("\n Informações da pessoa")
print(f"nome: {pessoa ['nome']}")
print("idade:", pessoa ["idade"])
print("cidade:", pessoa ["cidade"])
print("profissão:", pessoa ["profissão"])


# print(f"""
# Informações da pessoa
# nome: {pessoa ['nome']}
# idade: {pessoa ['idade']}
# cidade: {pessoa ['cidade']}
# profissão: {pessoa ['profissão']}
# """)
