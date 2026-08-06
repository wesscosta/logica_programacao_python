"""
Solicite quatro notas, armazenando-as em uma lista. Ao final, apresente:

- todas as notas;
- maior nota;
- menor nota;
- média da turma.

Utilize as funções nativas da linguagem sempre que possível.
"""

notas = []

for i in range(4):
    nota = float(input(f"Digite a {i+1} nota: "))
    notas.append(nota)

print(f"Todas as notas são: {notas}")
print(f"A maior nota é: {max(notas)}")
print(f"A menor nota é: {min(notas)}")
print(f"A média da turma é: {sum(notas)/4:.1f}")
