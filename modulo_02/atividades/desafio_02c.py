quantidade = 0
total = 0
maior = None
menor = None
 
while True:
    venda = float(input("Digite o valor da venda (0 para encerrar): R$ "))
 
    if venda == 0:
        break
 
    quantidade += 1
    total += venda
 
    if maior is None:
        maior = venda
        menor = venda
    else:
        if venda > maior:
            maior = venda
        if venda < menor:
            menor = venda
if quantidade > 0:
    media = total / quantidade
 
    print("\n===== RESUMO DAS VENDAS =====")
    print(f"Quantidade de vendas: {quantidade}")
    print(f"Valor total vendido: R$ {total:.2f}")
    print(f"Valor médio das vendas: R$ {media:.2f}")
    print(f"Maior venda: R$ {maior:.2f}")
    print(f"Menor venda: R$ {menor:.2f}")
else:
    print("Nenhuma venda foi registrada.")
