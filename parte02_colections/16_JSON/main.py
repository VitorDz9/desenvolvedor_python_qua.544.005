#biblioteca
import json
import os 


#lista 
usuarios = []

#limpar terminal 
os.system("cls" if os.name == "nt" else "clear")

#loop
while True:
     #menu 
     print("1 - cadastrar novo usuário")
     print("2 - Gravar arquivo JSON")
     print("3- Abrir arquivo JSON")
     print("4 - Sair do Programa ")
     opcao =input("Opção desejada: ").strip()
     os.system("cls" if os.name == "nt" else "clear")
     match opcao:
        case"1":
            #novo dicionário
            usuario ={}

            #insere dados do usuario 
            usuario["nome"] = input("Informe o nome : ").strip().title()
            usuario["idade"]= int(input("Informe sua idade:"))
            usuario["email"]=input("Informe seu email:").strip().title()
            usuario["cpf"]=input("Informe seu CPF: ").strip()
            usuario["telefone"]= input("Informe o telefone:").strip()

            #adicionar usuário na lista 
            usuarios.append(usuario) # adicionar um item na lista ---> append
            os.system("cls" if os.name == "nt" else "clear")

            #mensagem de confirmação
            print(f"{usuario.get('nome')} cadastrado com sucesso!") 
            continue
        case"2":
            #exibi os usuarios cadastrados
            for usuario in usuarios:
                for chave, valor in usuario.items():
                   print(f"{chave.capitalize()}: {valor}")
                print(f"{'-'*40}")
             #perguntar o usuário se deseja prosseguir 
                prosseguir= input("Deseja gravar os dados? (s/n)").strip().lower()   
                if prosseguir == "s":
                    os.system("cls") if os.name == "nt" else "clear"
                    arquivo = input("Informe o valor do arquivo :").strip()
                with open(f"16_JSON/{arquivo}.json","w",encoding="utf-8") as f:
                     json.dump(usuarios, f)
                print("Arquivo json gravado com sucesso  ") 
                continue
            else :os.system("cls" if os.name == "nt" else "clear")
            continue
        case"3":
             os.system("cls" if os.name == "nt" else "clear")
             try:
                 #informe o nome do arquivo desejado 
                 abrir= input("Informe o nome do arquivo que deseja abrir:").strip()


                 #abre o arquivo
                 with open(f"16_JSON?{abrir}.json", "r",encoding="utf-8") as f:
                     usuarios = json.load(f)
                 #exibir os dados do arquivo 
                 for usuario in usuarios:
                     for chave , valor in usuario.items():
                         print(f"{chave.capitalize()}: {valor}")
                     print(f"{'-'*40}")
                     continue
             except Exception as e:
                 print(f"Não foi possível abrir o arquivo. {e}.")
                 continue
        case"4":
             break
        case _:
             print("Opção Inválida")
               