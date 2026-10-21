#Tupla
dias_da_semana=(
    "Domingo" ,
    "Segunda-Feira",
    "Quarta-Feira",
    "Quinta-Feira",
    "Sexta-Feira",
    "Sábado",
)

for dia in dias_da_semana:
    print(dia)

#NOTE - se tentar alterar a tupla , o programa da erro . Exemplo
try:
    dias_da_semana.sort()
    for dia in dias_da_semana:
        print(dia)
except Exception as e:
    print(f"Não foi possivel ordenar.{e}.")
finally:
    print("Programa encerrado.")
