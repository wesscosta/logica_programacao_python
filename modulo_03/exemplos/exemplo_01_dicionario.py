aluno= {
    "nome"      :   "Fulano",
    "sobrenome" :   "de tal" ,
    "idade"     :   "18",
    "cidade"    :   "teresina",
    "profissao" :   "estudante" 
}

# for key in aluno:
#     print(aluno[])

# print(aluno.get("email", "Não tem essa key..."))

if aluno.get("email") and aluno.get("nome"):
    print (aluno["idade"], aluno["nome"])
else: 
    print("não tem!! ")

print ("alguma coisa para testar.......")
