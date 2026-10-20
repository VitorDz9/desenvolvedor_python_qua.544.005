# blibioteca

import os 


# lista 

nomes = ["Luís", "Rebeca","Vitor","Sara","Thaila","Felix","Esther"]

os.system("cls" if os.name == "nt" else "clear")

#loop 
while True:
    #exibir a lisa original
    for n, nome in enumerate(nomes):
        print(f"Índice {n}: {nome}")
    # menu 
    print("1- Alterar item da lista")
    print("2- Finalizar")
    opcao = input("Opção desejada: ").strip() # Informa opção desejada

#verificar a opção escolhida
        
    match opcao:
            
        case"1":
            #informa índice a ser alterado 
            indice = int(input("Informe o índice a ser alterado:"))
            # informar novo valor
            nomes [indice] = input("Informe novo nome :").strip().title()
            os.system ("cls" if os.name == "nt" else "clear ")
            print("Item da lista alterado com sucesso !")
            continue    
          
        case "2":
            os.system ("cls" if os.name == "nt" else "clear")
            #exibe a nova lista 
            for n, nome in enumerate(nomes):
                print(f"indice{n}: {nome}")
            break
        case _:
            print("Opção inválida")
            continue