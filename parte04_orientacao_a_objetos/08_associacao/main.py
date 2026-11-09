import os 

from model import Pessoa, Endereco


def limpar():
    os.system("cls" if os.name == "nt" else "clear")


def main():
    endereco = Endereco(cep="",uf="",cidade="",bairro="",logradouro="",complemento="",numero="")
    usuario = Pessoa(nome="",cpf="",email="",telefone="",endereco=endereco)

    limpar()

    usuario.nome=input("Informe o nome :").strip().title()
    usuario.cpf=input("Informe o CPF :").strip()
    usuario.email=input("Informe o E-mail :").strip().lower()
    usuario.telefone=input("Informe o telefone :").strip()
    endereco.uf = input("Iforme a UF:").strip().upper()
    endereco.cidade =input("Informe a cidade:").strip().title()
    endereco.bairro =input("Informe o bairro:").strip().title()
    endereco.logradouro =input("Informe o logradouro:").strip().title()
    endereco.complemento =input("Informe o complemento: ")
    endereco.numero = input("Informe o número:").strip()

    #saída de dados
    usuario.exibir_dados()


if __name__ == "__main__":
    main()
