import os 
#variaveis:

nome = (input("Digite seu nome:").strip().title())
massa= float(input("digite o seu peso em quilogramas(kg): ").replace(',','.'))
altura= float(input('Digite sua altura em metros:').replace(',','.'))

#calcular o valor da imc 
imc= massa/(altura**2)

# exibir valor de imc 
print(f"{nome},seu IMC é {imc:.2f}!")

if imc < 18.5:
    print(f"{nome} está abaixo do peso.")
elif imc < 25:
    print(f'{nome} possui peso adequado.')
elif imc < 30 :
    print(f'{nome} possui sobrepeso.') 
elif imc < 35:
    print(f'{nome}possui ibesidade grau I') 
elif imc <40:
    print(f'{nome}possui obesidade grau II')
else :
    print("Você está com obesidade mórbida")