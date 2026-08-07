# Desenvolva um programa que permita cadastrar vários alunos. Para cada estudante, informe seu nome e quatro notas. Ao final do cadastro, apresente um relatório contendo:

# - nome de cada aluno;
# - média final;
# - situação (Aprovado, Recuperação ou Reprovado);
# - maior média da turma;
# - menor média da turma;
# - média geral da turma.

# Utilize listas, estruturas condicionais e laços de repetição para organizar a solução.
alunos = []
medias =[]
situacoes = []

while True:
    print('\n1 - Cadastrar aluno')
    print('2 - Encerrar programa')
    
    opcao = input('Selecione uma opção: ')
    
    if opcao.isdecimal() == True:
        opcao = int(opcao)
    else:
        print('\nOpção invalida. Selecione 1 ou 2.')
        continue
    
    match opcao:
        case 1 :
            aluno = input('\nInforme o nome do aluno: ')
            alunos.append(aluno)

            for i in range (4):
                media += float(input(f'Informe a {i+1}ª nota do aluno: '))

            media = media / 4
            medias.append(media)
            if media >= 7:
                situacoes.append('Aprovado')
            elif media < 5:
                situacoes.append("Reprovado")
            else:
                situacoes.append('Recuperação')
        case 2:
            print('Programa encerrado! Abaixo o relatório completo de cada aluno')
            break
        case _:
            print('\nOpção inválida.')

for aluno,media,situacao in zip(alunos,medias,situacoes):
    print('\nRelatório do aluno: ')
    print(f'Aluno: {aluno}')
    print(f'Media: {media:.2f}')
    print(f'Situação: {situacao}')

print('\n: : : : RELATORIO DA TURMA : : : :')
print(f'Maior média da turma: {max(medias):.1f}')
print(f'Menor média da turma: {min(medias):.1f}')
print(f'Média geral da turma: {(sum(medias) / len(alunos)):.1f}')
