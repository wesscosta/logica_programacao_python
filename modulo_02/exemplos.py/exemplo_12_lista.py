# lista = [2 ,3, 4 ,5 ,6 ,7 ,8] 


# print(sum(lista))


# alunos = [
#     "Ana",
#     "Carlos",
#     "Maria",
#     "Fulana"
# ]

# medias = [
#     8.5,
#     7.0,
#     9.2,
#     0
# ]

# for aluno, media in zip(alunos, medias):
#     print(f"{aluno}: {media}")


produtos = [
    "Mouse",
    "Teclado",
    "Monitor",
    "Teclado",
    "Gabinete",
    "Teclado",
]

while "Teclado" in produtos:
    produtos.remove("Teclado")

    
print(produtos)
