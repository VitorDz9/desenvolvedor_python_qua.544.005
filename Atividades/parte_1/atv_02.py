#importa a biblioteca 
import os

#limpar terminal 
os.system("cls" if os.name=="nt" else "clear")

#dados 
nome = input("Informe seu nome : ").strip().title()
idade = int(input("Informe sua idade :"))
idade_minima = None

#loop
while True :
# menu de filmes 
    print(f"{('-')*20} CINE COBRA {'-'*20}")
    print("Sala 1 - A Roda Quadrada - LIvre")
    print("Sala 2 - A Volta dos Que Não Foram - 12 anos ")
    print("Sala 3 - As traças do Rei Careca - 14 anos ")
    print("Sala 4 - Peira em Alto Mar - 16 anos ")
    print("Sala 5 - A Vingança do Peixe Frito - 18 anos ")

  #usuário informa a sala do filme desejado 

    sala= input("Sala desejada:").strip()

    #verificar a idade minima do filme

    match sala:
        case"1":
            idade_minima=0
        case"2":
            idade_minima=12
        case"3":
            idade_minima=14
        case"4":
            idade_minima=16
        case"5":
            idade_minima=18
        case _:
            print("Sala inexistente.") 
            idade_minima=idade+1
    #verificar a idade 
    if idade >= idade_minima:
        print(f"Ingresso impresso para {nome}")
        print("Tenha um bom filme !")
        break
    else:
        os.system("cls" if os.name ==  "nt" else "clear")
        print(f"Ingresso negado para {nome}")
        print("Você não possui idade minima para ver o filme") 
        print("Por favor , escolha outro filme:")
    continue 