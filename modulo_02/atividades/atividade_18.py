"""
Cadastre as notas de dez estudantes.

Ao final:

- apresente todas as notas em ordem crescente;
- apresente todas as notas em ordem decrescente;
- informe a maior nota;
- informe a menor nota;
- informe a média da turma.
"""

notas = []

for i in range(10):
    nota = float(input(f"nota{i + 1}: "))
    notas.append(nota)
notas.sort()
print(notas)
notas.sort(reverse = True)
print(notas)
media = sum(notas) / len(notas)
print(f"media: {media:.1f}")
print(max(notas))
print(min(notas))
