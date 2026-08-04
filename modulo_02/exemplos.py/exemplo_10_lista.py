# Crie um loop infinito e armazene nome, cidade, idade das pessoas e encerre ao digitar sair, apois isso imprima

# iniciando variaveis
nomes = []
cidades = []
idades = []
i = 1

# alimentando a lista
while True:
    nome =  input(f"Digite o nome  da {i}º pessoa: ")
    if nome.lower() == "sair":
        break
    
    cidade =  input(f"Digite o cidades  da {i}º pessoa: ")
    if cidade.lower() == "sair":
        break
    
    idade =  input(f"Digite o idade  da {i}º pessoa: ")
    if idade.lower() == "sair":
        break
     
    nomes.append(nome)
    cidades.append(cidade)
    idades.append(idade)
    
    i+=1


# printando
if len(nomes) != 0:
    for j in range(len(nomes)):
         print (f"{nomes[j]} - {cidades[j]} - {idades[j]}")
else:
    print("Lista vazia")
