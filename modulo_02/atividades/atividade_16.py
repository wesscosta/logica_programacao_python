"""
Cadastre o nome de cinco alunos e a média final de cada um.

Após o cadastro, apresente um relatório contendo:

- nome;
- média;
- situação (Aprovado, Recuperação ou Reprovado).

Ao final, informe:

- quantidade de aprovados;
- quantidade de alunos em recuperação;
- quantidade de reprovados. 
"""
alunos = []
medias =[]
situacao_geral = []

for i in range (5):
    aluno = input('Informe o nome do aluno: ')
    alunos.append(aluno)
    media = float(input('Informe a media do aluno: '))
    medias.append(media)
    
    if media >= 7:
        situacao_geral.append('Aprovado'.lower())
    elif media < 5:
        situacao_geral.append('Reprovado'.lower())
    else:
        situacao_geral.append('Recuperação'.lower())

print('\n : : : : : Relatório da Turma : : : : :')
print(f'Alunos aprovados: {situacao_geral.count('aprovado')}')
print(f'Alunos reprovados: {situacao_geral.count('reprovado')}')
print(f'Alunos em recuperação: {situacao_geral.count('recuperação')}')
