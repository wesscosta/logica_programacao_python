"""Desenvolva um programa que permita cadastrar vários alunos. Para cada estudante, informe seu nome e quatro notas. Ao final do cadastro, apresente um relatório contendo:

- nome de cada aluno;
- média final;
- situação (Aprovado, Recuperação ou Reprovado);
- maior média da turma;
- menor média da turma;
- média geral da turma.

Utilize listas, estruturas condicionais e laços de repetição para organizar a solução."""


alunos = []
medias = []
situacoes = []

while True:
    print(" 1 cadastrar aluno")
    print(" 2 Encerrar programa ")
    
    opcao = input(f"Escolha a opção: ")
    
    match opcao:
        case "1":
            aluno = input("Nome do aluno: ")
            alunos.append(aluno)
            media = 0
            for i in range(4):
                media += float(input("Nota do aluno: "))
            media = media / 4
            medias.append(media)
            
            if media >= 7:
               situacoes.append("Aprovado")
               
            elif media < 5:
                situacoes.append("Reprovado" ) 
                
            else: 
                situacoes.append("Recuperaçao")
                
        case "2":
            print('Programa encerrado.')
            break
        
        case _:
            print("Opção Invalida")

print('::::::: Relatorio ::::::::')
for aluno,media,situacao in zip(alunos,medias,situacoes):
    print(f"aluno: {aluno}")
    print(f"media: {media}")
    print(f"situacao: {situacao}")
    print("\n")

print('::::: Relatorio da turma :::::')
print(f"Maior media: {max(medias):.1f}")
print(f"Menor media: {min(medias):.1f}")
print(f"Media geral: {sum(medias) / len(alunos):.1f}")
