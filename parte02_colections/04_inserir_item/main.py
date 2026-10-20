#biblioteca

import os 
#lista vazia
tarefas = []

os.system("cls" if os.name == "nt" else "clear") # limpar terminal 

#loop

while True :
    #MENU 
    print("1- Inserir nova tarefa na lista ")
    print("2- Finalizar e exibir lista ")
    opcao = input("Opção desejada :").strip() # informar a opçâo desejada
    
    #Verifica a opção informada
    match opcao:
        case"1":   
            nova_tarefa = input("Informe a nova tarefa: ")   #usuario informa novo item da lista
            tarefas.append(nova_tarefa) # Insere o item que o usuario digitou na lista - append
            continue # retorna para o inicio do loop
        case"2":
            os.system("cls" if os.name == "nt" else "clear")

            #exibi a lista
            for n, tarefa in enumerate (tarefas, start=1):
                print(f"{n}° tarefa:{tarefa}")
            break # encerrar o loop 
        case _:
            print("Opção Inválida.")

