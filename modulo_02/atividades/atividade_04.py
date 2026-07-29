# ## Atividade 04 — Menu do sistema

# Crie um menu com as opções:
#     1 - Novo cadastro
# 2 - Consultar cadastro
# 3 - Atualizar cadastro
# 4 - Remover cadastro

# Utilize match-case para apresentar uma mensagem correspondente à opção escolhida e trate entradas inválidas.

opcao = int(input("""
---menu---
1 - Novo cadastro
2 - Consultar cadastro
3 - Atualizar cadastro
4 - Remover cadastro
"""))

match opcao:
     case 1 :
         print("cadastro concluindo")
     case 2 :
         print("cadastro achado") 
     case 3 :
         print("cadastro atualizado")
     case 4 :
         print("cadastro removido")           
     case _:
         print("opcao invalido")

print("\nfim algoritmo")    
