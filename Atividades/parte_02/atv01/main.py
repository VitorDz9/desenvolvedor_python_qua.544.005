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
                print("Nenhum usuário cadastrado!")
            else:
                for usuario in usuarios:
                    print("--------------------------")
                    print(f"Nome:{usuario['nome']}")
                    print(f"Email:{usuario['email']}")
                    print(f"Telefone:{usuario['telefone']}")
                    print(f"CPF:{usuario['CPf']}")
        case"3":
            if usuarios==[]:
                print("Nenhum usuário cadastrado!")
            else:
                cpf_busca = input("Digite o Cpf do usuário que deseja alterar:")
                encontrado = False 
                for usuario in usuarios:
                    if usuario["cpf"]==cpf_busca:
                        print("Digite os novos dados:")
                        usuario["nome"]=input("Novo nome:")

                        usuario["email"]=input("Novo email:")
                        usuario["telefone"]=input("Novo telefone:")
                        usuario["cpf"]=input("Novo CPF:")

                        print("Usuário alterado com sucesso!")
                        encontrado = True
                        break
                if encontrado==False:
                    print("Usuário não encontrado!")
        case"4":
            if usuario==[]:
                print("Nenhum usuário cadastrado!")
            else:
                cpf_busca=input("Digite o CPF do usuário que deseja excluir:")
                encontrado= False

                for usuario in usuarios:
                    if usuario["cpf"]== cpf_busca:
                        usuarios.remove(usuario)
                        print("Usuário excluido com sucesso!")
                        encontrado=True
                        break
                    if encontrado==False:
                        print("Usuário não encontrado")


        case"5":
            print("Programa encerrado")
            break
        case"6":
            with open("usuarios.json", "w", encoding="utf-8") as arquivo:
                json.dump(usuarios, arquivo, indent=4,ensure_ascii=False)
            print("Usuários gravados com sucesso!")  
                      
    