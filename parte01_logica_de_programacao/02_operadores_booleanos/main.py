'''
Operadores lógicos 
1- and= e (Duas ou mais condições sejam verdadeiras)
2- or= ou (2 Condições onde somente 1 é verdadeira)
3- not= não (Condição negativa )

O .replace é uma função ou método usado na programação e em editores de texto para substituir uma parte de um texto (uma palavra, letra ou sequência de caracteres) por outra.

'''
nome= input("Informe seu nome: ").strip().title()
idade = int(input("Informe sua idade : "))
altura = float(input("Informe sua altura em metros:").replace(',','.'))

#verificar se o pagamento possui os requisitos
if  idade >= 12 and altura >= 1.35:
    print(f"{nome} está autorizado a entrar.")
else:
    print(f"{nome} não está autorizado a entrar.")
