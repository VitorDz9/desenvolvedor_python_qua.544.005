#dicionario
usuario = {
    'nome': "Fulano de Tal",
    'idade':18,
    'email': "fulano@gmail.com"
}
#usuario informa a nome da nova chave 
nova_chave = input("Informe o nome da nova chave: ").strip().lower()
#usuario informa o valor da chave 
usuario[nova_chave] = input("Informe o valor da nova chave : ").strip()

#exibir o dicionario
for chave, valor in usuario.items():
    print(f"{chave.capitalize()}: {valor}")