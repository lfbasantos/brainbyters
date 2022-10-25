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
opt = int(input("Digite 1, 2 ou 3 ->"))
msg="Você selecionou %s." % opt 
print(msg)

# Variaveis
qtdC = 0
qtdT = 0
qtdP = 0
dadoVerde="CPCTPC"
dadoAmarelo="TPCTPC"
dadoVermelho="TPTCPT"
tubo="GYRGYRGYRGYRG"

# Verifica opções
if opt == 1:
    qtd = int(input("Digite o número de jogadores ->"))
    if qtd > 1:
        # Sorteando os Dados
        dado1 = random.choice(tubo)
        dado2 = random.choice(tubo)
        dado3 = random.choice(tubo)
        if dado1 == "Y":
            dado1 = "Amarelo"
        elif dado1 == "G":
            dado1 = "Verde"
        else:
            dado1 = "Vermelho"
        if dado2 == "Y":
            dado2 = "Amarelo"
        elif dado2 == "G":
            dado2 = "Verde"
        else:
            dado2 = "Vermelho"
        if dado3 == "Y":
            dado3 = "Amarelo"
        elif dado3 == "G":
            dado3 = "Verde"
        else:
            dado3 = "Vermelho"
        msg = "Dados: {}, {} e {}".format(dado1, dado2, dado3)
        print(msg)

        # Sorteia
        # Dado 1
        if dado1 == "Verde":
            res1 = random.choice(dadoVerde)
        elif dado1 == "Amarelo":
            res1 = random.choice(dadoAmarelo)
        else:
            res1 = random.choice(dadoVermelho)
        # Dado 2
        if dado2 == "Verde":
            res2 = random.choice(dadoVerde)
        elif dado2 == "Amarelo":
            res2 = random.choice(dadoAmarelo)
        else:
            res2 = random.choice(dadoVermelho)
        # Dado 3
        if dado3 == "Verde":
            res3 = random.choice(dadoVerde)
        elif dado3 == "Amarelo":
            res3 = random.choice(dadoAmarelo)
        else:
            res3 = random.choice(dadoVermelho)
        
        # Contabiliza
        # Res 1
        if res1 == "C":
            qtdC = qtdC + 1
        elif res1 == "T":
            qtdT = qtdT + 1
        else:
            qtdP = qtdP + 1
        # Res 2
        if res2 == "C":
            qtdC = qtdC + 1
        elif res2 == "T":
            qtdT = qtdT + 1
        else:
            qtdP = qtdP + 1
        # Res 3
        if res3 == "C":
            qtdC = qtdC + 1
        elif res3 == "T":
            qtdT = qtdT + 1
        else:
            qtdP = qtdP + 1
        
        # Resultado 
        msg = "Cérebros - {}, Pegadas - {}, Tiros - {}".format(qtdC, qtdP, qtdT)
        print(msg)
    else: 
        print("Este jogo precisa de pelo menos 2 jogadores.")

