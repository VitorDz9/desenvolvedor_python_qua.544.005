#dicionario
usuario={
    'nome':"Luís",
    'idade':19,
    'email':"luisguilherme67@gmail.com",
    'telefone':"(61) 99999-9999",   
    'endereço':"Campo da Esperança"
}

#exibi a lista original
for chave, valor in usuario.items():
    print(f"{chave}:{valor}")

    #informe a chave a ser deletada
chave_escolhida = input("Informe a chave a excluir: ").strip().lower()

#DELETAR CHAVE 
del usuario[chave_escolhida]

#re-exibir o novo dicionario
for chave, valor in usuario.items():
    print(f"{chave}:{valor}")