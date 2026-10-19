#lista de cidades 
cidades=["Rio de Janeiro","Brasília","São Paulo","Goiânia", "Cuiabá","João Pessoa","Natal","Aracaju","Campinas","São José dos Campos","Ouro Preto","Tiradentes","Ribeirão Preto","Sorriso","Foz do Iguaçu","Gramado","Canela","Porto Seguro"]

#ordena a lista 
cidades.sort()

#exibe a lista em ordem alfabetica
for cidade in cidades :
    print(cidade)

    print()
    #reverse a lista
    cidades.sort(reverse=True)

    #exibe uma lista em ordem reversa
    for cidade in cidades :
        print(cidade)

    