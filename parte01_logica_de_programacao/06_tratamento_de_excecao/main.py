#tratamento de exceção
try: #tente
    nome= input("infome seu nome :").strip().title()
    idade= int(input("Digite sua idade:"))

    print(f"Nome do usuário: {nome}.")
    print(f"Idade do usuário: {idade} anos.")

except Exception as e: #exeto
    print(f"Não foi possível executar a ação! {e}.") 
finally:
    print("Programa dinalizado com sucesso!")
    