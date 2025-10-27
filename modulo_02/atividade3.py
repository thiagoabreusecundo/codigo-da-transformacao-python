# =========================================================
# ATIVIDADE 3: Programa de saudação personalizada
# =========================================================

# 1. Pede o nome do usuário e armazena o que foi digitado na variável 'nome'
# A função input() pausa o programa e espera o usuário digitar e apertar Enter.
nome = input("Por favor, digite seu nome: ")

# 2. Constrói a mensagem de saudação
# Usamos a formatação de string (f-string) para incorporar o valor da variável 'nome'
mensagem = f"Olá, {nome}! Seja muito bem-vindo(a) ao mundo Python. É um prazer ter você aqui!"

# 3. Exibe a mensagem personalizada na tela
print("-" * 50) # Linha divisória para melhor visualização
print(mensagem)
print("-" * 50)

# Demonstração extra (Opcional): Mostra que a entrada do usuário é sempre uma string
print("\nNota: O dado que você digitou é do tipo:", type(nome))