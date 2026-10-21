# DicionarioÉ uma lista em que as informações são organizadas por palavra chave 
usuario= {
    'nome':"Marcos Vinicios",
    'idade':27,
    'altura':1.72,
    'email':"marcosv10@gmail.com",
    'cpf':"012.456.456-78",
    'telefone':"(61) 99999-9999"
}

#exibir valor especifico
print(f"Nome: {usuario['nome']}")    
print(f"E-mail: {usuario.get('email')}")

#percorre o dicionario
for chave, valor in usuario.items():
    print(f"{chave.capitalize()}: {valor}.")