frutas = ["uva","pera", "Tomate", "Abacaxi"]

print(frutas)
outra_fruta = input("Digite uma fruta: ")
frutas.append(outra_fruta)

print("Atualização")
print(frutas)

frutas[0] = "Uva"

print("Atualização 2")
print(frutas)

#['Uva', 'pera', 'Tomate', 'Abacaxi', 'Goiaba']
for fruta in frutas:
    print(fruta)


