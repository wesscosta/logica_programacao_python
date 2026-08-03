quantidade = 0
total = 0
maior = 0
menor = 0
 
while True:
    venda = float(input("digite o valor da venda (0 para encerrar): "))
 
    if venda == 0:
        break
    quantidade += 1
    total += venda
    
    if quantidade == 1:
        maior = venda
        menor = venda
    else:
        if venda>maior:
            maior = venda
        if venda < menor:
            menor = venda
            
if quantidade > 0:
    media = total / quantidade
    print("quantidade de vendas:", quantidade)
    print("valor total vendido:", total)
    print(f"valor medio das vendas: {media:.2f}")
    print("maior venda registrada:", maior)
    print("menor venda registrada:", menor)
else:
    print("nenhuma venda foi registrada")
