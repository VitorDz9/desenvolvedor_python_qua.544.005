#bibliotecas
import os
#declaração de função

def boa_vindas(nome):
    print(f"{nome},seja bem-vindo")

def limpar():
    os.system("cls" if os.name== "nt" else "clear")

#algoritimo principal
nome = input("Informe seu nome :").strip().title()
boa_vindas(nome)