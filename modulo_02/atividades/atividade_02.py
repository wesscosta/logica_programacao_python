"""
Solicite a nota final de um estudante e informe sua situação conforme os critérios abaixo:
- nota maior ou igual a 7: aprovado;
- nota maior ou igual a 5 e menor que 7: recuperação;
- nota menor que 5: reprovado.
"""

nota_final = float(input("Digite a nota final: "))

if nota_final >= 7:
    print("Aluno aprovado")
elif nota_final >= 5:
    print("Aluno de recuperação ")
else: 
    print("Aluno reprovado!")
