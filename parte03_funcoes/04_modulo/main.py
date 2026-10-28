# importar modulo 
import modulo


#algoritmo principal
modulo.limpar()
while True:
    print("1 - calcular área do quadrilátero")
    print("2 - Calcular área do circulo")
    print("3 - Calcular comprimento do círculo")
    print("4 - Sair do programa")
    opcao = input("Opção desejada:").strip()
    match opcao:
        case"1":
            b = float(input("Informe a base:").replace(",","."))
            h = float(input("Informe a altura:").replace(",","."))
            a = modulo.a_quad(b,h)
            print(f"Área do qiadrilátero: {a}.")
            continue
        case"2":
            r = float(input("Informe o raio:").replace(",","."))
            a = modulo.a_circulo(r)
            print(f"Área do círculo: {a}.")
            continue
        case"3":
            r = float(input("Informe o raio:").replace(",","."))
            a = modulo.comprimento_circulo(r)
            print(f"Comprimento do circulo {a}")
            continue
        case"4":
            break
        case _:
            print("Opção Inválida.")