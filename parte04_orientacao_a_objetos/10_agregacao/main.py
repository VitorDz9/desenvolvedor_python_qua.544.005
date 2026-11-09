import os

from model import Empresa , Departamentos


def limpar():
    os.system("cls" if os.name == "nt" else "clear")


def main():
    departamento = Departamentos(nome="")
    empresa = Empresa(razao_social="",nome_fantasia="",cnpj="",departamento=departamento)

    limpar()
    print("Defina os dados da empresa:")
    empresa.razao_social=input("Informe a razão socail :").strip()
    empresa.nome_fantasia = input("Informe o nome: ").strip()
    empresa.cnpj= input("Informe o CNPJ:").strip()
    empresa.departamento.nome= input("Informe o departamento em que traalha: ").strip()

    limpar()
    print(empresa.detalhes())


if __name__ == "__main__":
    main()