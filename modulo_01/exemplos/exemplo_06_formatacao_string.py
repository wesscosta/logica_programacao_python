nome = "Fulano"
idade= 18
cidade="Teresina"
curso="Técnico em Desenvolvimento de Sistemas"
#Olá, Fulano você tem 18 anos, mora em Teresina e cursa Técnico em Desenvolvimento de Sistemas!

#Padrão
print("Olá,",nome,"você tem", idade, "anos, mora em",cidade, "e cursa", curso,"!")

#Concatenação
print("Olá, "+ nome +" você tem "+str(idade)+ " anos, mora em "+cidade+ " e cursa "+ curso+ "!")

#.format
print("Olá, {} você tem {} anos, mora em {} e cursa {}!".format(nome,idade,cidade,curso))

#F-strings (recomendado e mais utilizado)
print(f"Olá, {nome} você tem {idade} anos, mora em {cidade} e cursa {curso}!")

# %
print("Olá, %s você tem %s anos, mora em %s e cursa %s!" % (nome,18,cidade,curso))
