"""Crie um menu com as opções:

```
1 - Adicionar produto
2 - Remover produto
3 - Listar produtos
4 - Encerrar
```

Os produtos deverão ser armazenados em uma lista durante a execução do programa.

Utilize estruturas de repetição e `match-case` para controlar o menu."""

produtos=[]
while True:
    print("""
          1 - ADICIONAR PRODUTO
          2 - REMOVER PRODUTO 
          3 - LISTAR PRODUTO
          4 - ENCERRAR 
          """)
    opcao=input("DIGITE A OPÇÃO QUE VC DESEJA: ")    
    match opcao:
        case "1":
            produto = input("DIGITE O PRODUTO QUE DESEJA ADICIONAR: ")
            produtos.append(produto)
        
        case "2":
            produto = input("DIGITE O PRODUTO QUE DESEJA REMOVER: ")
            if produto in produtos:
                produtos.remove(produto)
                
        case "3":
            print(produtos)
            
        case "4":
            print("PROGRAMA ENCERRADO. ")
            break
        
    
