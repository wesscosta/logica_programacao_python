# ## Atividade 04 — Menu do sistema

# Crie um menu com as opções:
#     1 - Novo Cadastro
# 2 - Consultar Cadastro
# 3 - Atualizar Cadastro
# 4 - Remover Cadastro

# Utilize match-case para apresentar uma mensagem correspondente à opção escolhida e trate entradas inválidas.

opcao = int(input("""
---menu---
1 - Novo Cadastro
2 - Consultar Cadastro
3 - Atualizar Cadastro
4 - Remover Cadastro
"""))

match opcao:
     case 1 :
         print("Cadastro concluindo")
     case 2 :
         print("Cadastro achado") 
     case 3 :
         print("Cadastro atualizado")
     case 4 :
         print("Cadastro removido")           
     case _:
         print("Opcao invalido")

print("\nfim algoritmo")    
