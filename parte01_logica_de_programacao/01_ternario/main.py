#declaração de variáveis
nome=input("Digite seu nome:").strip().title()
idade= int(input("Informe sua idade : "))

# ====================================================================
# 🔥 COLA RÁPIDA: .strip() e .title()
# ====================================================================
# .strip() -> Apaga os espaços invisíveis apenas nas PONTAS do texto.
# .title() -> Deixa a PRIMEIRA letra de cada palavra MAIÚSCULA.

# ⚠️ IMPORTANTE: Strings são imutáveis! Para salvar a mudança, reatribua:
# texto = texto.strip().title()  # Junta e salva os dois comandos
# ====================================================================


#Operador ternário
print(f"{nome} {'é maior de idade'if idade >=18 else 'é menor de idade'}.")


'''
# ====================================================================
# 🔥 RESUMO: IF TERNÁRIO DENTRO DE F-STRING
# ====================================================================
# Faz um "if/else" de uma linha só direto dentro do print.

# ⚠️ REGRA DE OURO DAS ASPAS:
# Se a f-string usa aspas DUPLAS por fora -> f"..."
# O texto do if/else DEVE usar aspas SIMPLES por dentro -> '...'
# Misturar aspas iguais quebra o código (SyntaxError).

# Exemplo:
nome, idade = "Carlos", 17
print(f"{nome} {'é maior de idade' if idade >= 18 else 'é menor de idade'}.")
# Saída: Carlos é menor de idade.
# ====================================================================
'''