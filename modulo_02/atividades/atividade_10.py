#Desenvolva um programa que solicite o nome de cinco alunos, armazenando-os em uma lista. Ao final, apresente todos os nomes cadastrados.

alunos = []

for i in range(5):
    aluno = input(f"digite o  nome do {i+1}º aluno: ")
    alunos.append(aluno)

print(alunos)
