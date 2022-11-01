"""
Luiz Filipe Bandeira Alves dos Santos
2022-10
lfbasantos@gmail.com
PUC/PR - Raciocínio Computacional
Python 3.11.0
"""

#
## imports
import random 
import os 

#
## Inicio - Main
while True:
    os.system('cls')
    #
    ## Tela Inicial - Menu Principal
    menuInicial = False
    print('Seja bem-vindo(a) ao Brain Byters!')
    print('Selecione uma opção:')
    print('1 - Iniciar')
    print('2 - Manual')
    print('3 - Sair')
    while True:
        try:
            opt = int(input("Digite 1, 2 ou 3 ->"))
            if opt >= 1 and opt <= 3:
                break 
            else:
                print("Digite um número de 1 a 3")
        except ValueError:
            print("Digite um número de 1 a 3")
    #
    ## Encerra
    if opt == 3:
        print("Jogo encerrado.")
        break 

    #
    ## Manual (TBD)
    elif opt == 2:
        print("TBD") 
        print("TBD")
        print("TBD")
        print("TBD")
        print("TBD")
        print("TBD")
        print("TBD")
        input("Voltar->")
        continue 

    #
    ## Inicia fluxo da partida
    else:
        while True and menuInicial == False:
            #
            ## Variaveis
            qtdC = 0
            qtdT = 0
            qtdP = 0
            dadoVerde="CPCTPC"
            dadoAmarelo="TPCTPC"
            dadoVermelho="TPTCPT"
            tubo=[
                dadoVerde,dadoAmarelo,dadoVermelho,dadoVerde,
                dadoAmarelo,dadoVermelho,dadoVerde,dadoAmarelo,
                dadoVermelho,dadoVerde,dadoAmarelo,dadoVermelho,dadoVerde
            ]
            jogadas=[]
            jogadores=[]

            #
            ## Verifica quantidade de jogadores
            while True:
                try:
                    qtd = int(input("Digite o número de jogadores ->"))
                    if qtd > 1:
                        break 
                    else:
                        print("Este jogo precisa de pelo menos 2 jogadores.")
                except ValueError:
                    print("Valor invalido")
            
            #
            ## Solicita nomes dos jogadores
            c=1
            while c < qtd+1:
                nome=str(input("Digite o nome do jogador {} ->".format(c))) 
                jogadores.append(nome)
                c = c + 1

            #
            ## Processa turnos
            indexJogador = 1
            while True:
                #
                ## Verifica se acabou a lista de jogadores e reinicia
                if indexJogador > qtd:
                    indexJogador = 1
                
                #
                ##
                os.system('cls')
                print("Rodada do Jogador {}, {}".format(indexJogador, jogadores[indexJogador-1]))
                
                #
                ## Opções
                while True:
                    try:
                        print("Selecione uma opção:")
                        print("1 - Jogar Rodada")
                        print("2 - Passar")
                        print("3 - Encerrar Jogo")
                        opt = int(input("->"))
                        if opt == 1 or opt == 2 or opt == 3:
                            break 
                        else:
                            print("Digite número 1, 2 ou 3")
                    except ValueError:
                        print("Valor invalido")
                
                #
                ## Rodadas
                os.system('cls')
                if opt == 1:
                    #
                    ## Zerando lista no início da rodada
                    jogadas.clear()

                    #
                    ## Sorteando os Dados
                    for i in [0,1,2]:
                        idx = random.randint(0, 12)
                        dado = tubo[idx]

                        #
                        ## 
                        if dado == "CPCTPC":
                            print("Dado Verde")
                        elif dado == "TPCTPC":
                            print("Dado Amarelo")
                        else:
                            print("Dado Vermelho")
                        
                        #
                        ##
                        jogadas.append(dado)

                        #
                        ##


                    #
                    # Sorteia e Verifica faces dos dados
                    for jogada in jogadas:
                        lancamento = random.randint(0,5)
                        if jogada[lancamento] == "C":
                            print("Você comeu um cérebro")
                            qtdC = qtdC + 1
                        elif jogada[lancamento] == "T":
                            print("Você levou um tiro.")
                            qtdT = qtdT + 1
                        else:
                            print("Uma vítima fugiu")
                            qtdP = qtdP + 1

                    # Resultado 
                    msg = "Score: Cérebros - {}, Pegadas - {}, Tiros - {}".format(qtdC, qtdP, qtdT)
                    print(msg)
                    pause=input("Enter....")

                    #
                    ## Valida se venceu ou morreu
                    if qtdT > 2 or qtdC > 12:
                        if qtdT > 2:
                            print("Headshot! Você já era.")
                        if qtdC > 12:
                            print("Parabéns Brain Byter você venceu!")
                
                #
                ## Passa
                if opt == 2:
                    qtdC=0
                    qtdP=0
                    qtdT=0
                    indexJogador = indexJogador + 1
                    continue

                #
                ## Encerra 
                if opt == 3:
                    menuInicial = True
                    break