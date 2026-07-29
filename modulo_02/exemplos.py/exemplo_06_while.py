contador = 1

while contador <= 50:
    
    if contador % 5 == 0 :
        contador += 1
        continue
    
    print(contador)
    
    comando = input("Digite 'sair' para finalizar: ")
    if comando.lower() == "sair":
        break #parar
    
    contador += 1

print("Programa encerrado.")
