# =========================================================
# DESAFIO EXTRA: Saudação com Nome e Hora Atual
# =========================================================

# 1. Importa a biblioteca (módulo) datetime
# Este módulo contém classes para manipulação de data e hora
import datetime

# 2. Pede o nome do usuário
nome = input("Por favor, digite seu nome: ")

# 3. Obtém a hora e a data atual
# datetime.datetime.now() retorna um objeto que contém a data e hora atuais
momento_atual = datetime.datetime.now()

# 4. Formata a hora para um formato legível (Ex: 14:03:14)
# O método strftime é usado para formatar o objeto de tempo
# %H: Hora (24h), %M: Minuto, %S: Segundo
hora_formatada = momento_atual.strftime("%H:%M:%S")

# 5. Constrói a mensagem de saudação completa
# Combina o nome e a hora formatada
mensagem_completa = f"Olá, {nome}! A hora atual é {hora_formatada}. Seja bem-vindo(a)!"

# 6. Exibe a mensagem na tela
print("\n" + "=" * 60)
print(mensagem_completa)
print("=" * 60)