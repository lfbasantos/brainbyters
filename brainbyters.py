"""
Luiz Filipe Bandeira Alves dos Santos
2022-10
lfbasantos@gmail.com
PUC/PR - Raciocínio Computacional
"""

# imports
import random 

# Tela Inicial - Menu Principal
msg = 'Seja bem-vindo(a) ao Brain Byters!'
print(msg)
msg = 'Selecione uma opção:'
print(msg)
msg = '1 - Iniciar'
print(msg)
msg = '2 - Ajuda'
print(msg)
msg = '3 - Sair'
print(msg)
opt = input("Digite 1, 2 ou 3 ->")
msg="Você selecionou %s." % opt 
print(msg)

# Verifica opções
if opt == 1:
    qtd = input("Digite o número de jogadores ->")
    if qtd > 1:
        # Definindo os Dados
        dadoVerde="CPCTPC"
        dadoAmarelo="TPCTPC"
        dadoVermelho="TPTCPT"

        # Sorteando os Dados
        dado1 = random.choice(dadoVerde)
        print(dado1)

