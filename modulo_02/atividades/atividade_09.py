# Crie um programa que continue solicitando usuário e senha até que os valores estejam corretos.

#Opção 01
USUARIO = "admin"
SENHA = "python123"

usuario = input("Digite o usuario: ") 
senha = input("Digite a senha: ") 

while usuario != USUARIO or senha != SENHA:
        print("usuário ou senha incorretos, tente novamente!")
        
        usuario = input("Digite o usuario: ") 
        senha = input("Digite a senha: ") 
print("login realizado com sucesso! ")

#Opção 02

USUARIO = "admin"
SENHA = "python123"

while True:
    usuario = input("Digite o usuário: ")
    senha = input("Digite a senha: ")
        
    if usuario == USUARIO and senha == SENHA:
        print("login realizado com sucesso! ")
        break
    
    print("Senha Incorreta, tente novamente! ")
