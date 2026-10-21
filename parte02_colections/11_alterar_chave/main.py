#bibliotecas
import os

#dicionario

usuario = {
    'nome': "Thomas Turbano",
    'idade':40,
    'email':"arianagrande@gmail.com",
    'telefone':"(61) 94513-3682"

}

#limpar terminal
os.system("cls" if os.name == "nt" else "clear")

#loop
while True:
    #exibir dicionario
    for chave , valor in usuario.items():
        print(f"{chave}:{valor}")

    #informa o nome da chave
    chave_escolhida = input("Informe o nome da chave que deseja alterar ou Enter para encerrar:").strip().lower()
    #verficar se a chave é valida
    if chave_escolhida:
    #informa o novo valor 
        usuario[chave_escolhida]= input("Informe o novo valor: ").strip()
        continue
    else:
        break
