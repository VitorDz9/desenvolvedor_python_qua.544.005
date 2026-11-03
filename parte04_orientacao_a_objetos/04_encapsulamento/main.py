from model import Pessoa


def main():
    ususario= Pessoa(nome="", idade=0,cpf="",telefone="",email="")

    ususario.nome = input("Informe o nome :").strip().title()
    ususario.idade = input("Informe a idade:")
    ususario.cpf = input("Informe o CPF :").strip()
    ususario.telefone = input("Informe o telefone :").strip()
    ususario.email = input("Informe o email :").strip().lower()


    print(f"Nome :{ususario.nome}")
    print(f"Idade :{ususario.idade} anos")
    print(f"CPF :{ususario.cpf}")
    print(f"Telefone :{ususario.telefone}")
    print(f"Email :{ususario.email}")


if __name__ == "__main__":
    main()