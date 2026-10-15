#Importar as bibliotecas
import os
import time

#limpar o terminal
os.system("cls")

#declaração de variaveis 
n = int(input("Informe um número inteiro : "))

#contador
while n >=0:
    os.system("cls")
    print(f"{n}...")
    time.sleep(1)
    n-= 1 
print("BOOMM!!!!!!!")