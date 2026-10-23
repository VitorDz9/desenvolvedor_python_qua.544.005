#TODO:parte 02 atividade 01
'''
crie um programa que faça as seguintes operações :
-Cadastrar novo usuário(nome , email, telefone , cpf )
-Liste todos os usuários cadastrados 
-Alterar os dados de um usuário
-Excluir um usuário
-Grava os dados de todos os usuários em um .json 
-Abre arquivo .json e lista todos os usuários cadastrados nele 
'''
#bibliotecas 
import os 
import json 

#limpar terminal 
os.system("cls" if os.name == "nt" else "clear" )
 
usuarios=[]
while True:
    print("1 - Cadastrar usuário")
    print("2 - Listar usuários.")
    print("3 - Alterar usuários.")
    print("4 - Excluir usuários. ")
    print("5- Encerrar programa.") 
    print("6-Gravar dados em JSON")

    opcao = input("Escolha uma opção ")
    match opcao:
        case"1":
            nome = input("Informe o nome do usuário:").strip().title()
            email =input("Informe o email do usuário:").strip()
            telefone = input("Informe o telefone do usuário:").strip()
            cpf = input("Informe o CPF do usuário:").strip()

            usuario = {
                nome,
                email,
                telefone,
                cpf
            }
            usuarios.append(usuario)

            print("Usuário cadastrado com sucesso!")

            
        case"2":
            if usuarios ==[]:
                print("")
        case"3":
            print("Alterar usuários")
        case"4":
            print("Excluir usuários")
        case"5":
            print("Encerrar programa")
            break
        case _:
            print("Opção inválida!")
    
    