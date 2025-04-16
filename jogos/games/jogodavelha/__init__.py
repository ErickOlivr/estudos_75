import textos
import random
from games import ganhadorgeral

def jogodavelha ():
    cont = 1
    jog = 0
    comp = 0
    
    print(textos.exp_jogodavelha)
    print()
    while cont < 4:
        print(f'Rodada {cont} de 3.')
        print()
        while True:
            try:
                opcoes = input('Escolha entre X ou O: ').upper()
                if opcoes in ('X' 'O'):
                    jogador = opcoes
                    computador = 'O' if jogador == 'X' else 'X'
                    break
                else:
                  print('Escolha uma das opções.')
            except ValueError:
                print('Informe corretamente.')
                
        print(textos.velha) 
        ganhador= velha(jogador)
        if ganhador == jogador:
            print('O jogador venceu a rodada')
            jog+=1
        elif ganhador == computador:
            print('O Computador venceu a rodada')
            comp+=1
        elif ganhador == 'empate':
            print('Empate')
        cont+=1
    geral = ganhadorgeral(jog,comp)
    return geral


def velha(op):
    c = 0
    jogo=[' ',' ',' ',' ',' ',' ',' ',' ',' ']
    while ' ' in jogo:
        while True:
            try:
                escolha= int(input('Onde gostaria de jogar? Escolha entre 0 e 8: '))
                if escolha in range(0,9):
                    if jogo[escolha]== ' ':
                        jogo[escolha]= op
                        
                        lugar_livre = [i for i, valor in enumerate(jogo) if valor == ' ']
                        if lugar_livre:
                            computador = random.choice(lugar_livre)
                            
                            if op == 'X':
                                jogo[computador] = 'O'
                            elif op == 'O':
                                jogo[computador] = 'X'
                        print(f'''
{jogo[0]} | {jogo[1]} | {jogo[2]}
---------
{jogo[3]} | {jogo[4]} | {jogo[5]}
---------
{jogo[6]} | {jogo[7]} | {jogo[8]}''')
                        
                        vencedor = verificar_vitoria(jogo)
                        if vencedor:
                            return vencedor
                        break
                    else:
                        print('Posição já foi escolhida.')
            except ValueError:
                print('Informe um numero inteiro para escolher onde quer jogar.') 
                
    return 'empate'
        

def verificar_vitoria(jogo):
    comb = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),  # linhas
    (0, 3, 6), (1, 4, 7), (2, 5, 8),  # colunas
    (0, 4, 8), (2, 4, 6) #diagonais
    ]
    
    for a,b,c in comb:
        if jogo[a] == jogo[b] and jogo[b] == jogo [c] and jogo[a] != ' ':
            return jogo[a]
    
    return None
        