valor_da_venda = float
valor_total = 0
valor_medio = 0
vendas_realizadas = 0
maior_venda_registrada = 0
menor_venda_registrada = 999999

while valor_da_venda != 0:
    
    valor_da_venda = int(input("Informe o valor da venda ou digite zero para sair: "))
        
    if valor_da_venda == 0:
        print (f"quantidade de vendas realizadas: {vendas_realizadas}")
        print (f"valor total vendido: {valor_total}")
        print (f"valor medio das vendas: {valor_medio}")
        print (f"maior venda registrada {maior_venda_registrada}")
        print (f"menor venda registrada {menor_venda_registrada}")
        break
    
    if valor_da_venda >= maior_venda_registrada:
        maior_venda_registrada = valor_da_venda
        
    if valor_da_venda <= menor_venda_registrada:
        menor_venda_registrada = valor_da_venda
        
    vendas_realizadas += 1
    valor_total += valor_da_venda
    valor_medio = valor_total / v__endas_realizadas
