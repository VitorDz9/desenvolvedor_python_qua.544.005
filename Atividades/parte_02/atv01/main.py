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
#lista
usuarios=[]

#limpar terminal
os.system("cls" if os.name == "nt" else "clear")

#loop  
while True:
    #exibir menu
    print("1 - Cadastrar novo usuário")
    print("2 - Lista usuários cadastrados")
    print("3 - Alterar dados do usuário")
    print("4 - Excluir um usuário")
    print("5- Gravar todos os usuários em .json")
    print("6 - Abrir arquivo .json")
    print("7 - Sair do programa ")
    opcao = input("Opção desejada:").strip()
    os.system("cls" if os.name=="nt" else "clear")
    match opcao:
        case"1":
            #inicializar um novo dicionario
            usuario = {}
            #informa dados
            usuario['nome'] = input("Informe o nome do usuário:").strip().title()
            usuario['email']= input("Informe o email:").strip().title()
            usuario['telefone']=input("Informe o telefone:").strip().title()
            usuario['cpf']=input("Informe o CPF:").strip()

            #adicionar novo usuário a lista
            usuarios.append(usuario)
            os.system("cls"if os.name == "nt" else "clear")
            print(f"{usuario.get('nome')} cadastrado com sucesso")

            continue
        case"2":
            if usuarios:
                for i, usuario in enumerate(usuarios):
                    print(f"ID:{i}")
                    for chave,valor in usuario.items():
                        print(f"{chave.capitalize()}: {valor}.")
                print(f"{'-'*40}")
            else:
                print("Não foram encontrados usuários cadastrados.")
            
            continue
        case"3":
            try:
                indice = int(input("Informe o ID do usuário a atualizar:"))
                for chave, valor in usuarios[indice].items():
                    print(f"{chave.capitalize()}: {valor}.")
                chave = input("Qual chave deseja alterar o valor ?").strip().lower()
                usuarios[indice][chave] = input("Informe um novo valor:").strip()
                os.system("cls" if os.name == "nt" else "clear")
                print(f"Dados de {usuarios[indice][chave]} de {usuarios[indice].get('nome')}alterado com sucesso!")
                continue
            except Exception as e:
                print(f"Não foi possivel atualizar os dados. {e}.")
        case"4":
            try:
                indice =int(input("Informe o ID a ser excluido"))
                del usuarios[indice]
                os.system("cls") if os.name == "nt" else "clear"
                print("Usuários excluído com sucesso!")
                continue 
            except Exception as e   :
                print(f"Não foi possivel excluir. {e}") 
        case"5":
            arquivo = input("Informe o nome do arquivo:").strip()
            with open(f"atv01/{arquivo}.json","w",encoding="utf-8") as f:
                json.dump(usuarios, f) # dump = comando de gravar da biblioteca
            os.system("cls" if os.name == "nt" else "clear")
            print("Dados gravados com sucesso!")
            continue
        case"6":
            try:
                arquivo= input("Informe o arquivo que deseja abrir :").strip()
                with open(f"atv01/{arquivo}.json","r",encoding="utf-8") as f:
                    usuarios= json.load(f)
                os.system("cls" if os.name=="nt" else "clear")
                print("Dados importados com sucesso !")
                continue    
            except Exception as e:
                print(f"Não foi possivel abrir o arquivo. {e}.")
        case"7":
            break
        case _:
            print("Opção inválida.")
            continue
            
