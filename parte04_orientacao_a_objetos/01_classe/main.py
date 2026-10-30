#classe
class Pessoa :
    #construtor 
    def __init__(self,nome,idade,email,cpf):
        #atributos
        self.nome=nome
        self.nome=idade
        self.nome=email
        self.nome=cpf

    def exibir_dados(self):
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")
        print(f"Email: {self.email}")
        print(f"Cpf: {self.cpf}")
        
#Criar a pessoa
def main():
    #instaciar a classe (criar um objeto)
    usuario = Pessoa(nome="",idade=0,email="",cpf="")

    #Insere valores noa atributos
    usuario.nome = input("Informe o nome :").strip().title()
    usuario.idade = input("Informe a idade :").strip().title()
    usuario.email = input("Informe o email:").strip().title()
    usuario.cpf = input("Informe o cpf :").strip().title()

    #exibi os atributos na tela 
    usuario.ebibir_dados()
       
if __name__ == "__main__":
     main()