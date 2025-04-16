def ppt():
    import random, textos
    from games import ganhadorgeral
    opcoes = ('pedra', 'papel', 'tesoura')
    n = 1
    jogpoint = 0
    comppoint = 0
    sep = '-'*40
    print(textos.exp_ppt)
    print()
    while n < 4:
        print(f'Rodada {n} de 3')
        print()
        computador = random.choice(opcoes)
        while True:
            try:
                jogador = input('Escolha entre pedra, papel ou tesoura: ').strip().lower()
                if jogador in opcoes:
                    print(f'O computador escolheu {computador}')
                    if jogador == computador:
                        print('Empate.')
                        print(sep)
                        break
                    elif (jogador == "pedra" and computador == "tesoura") or \
                    (jogador == "papel" and computador == "pedra") or \
                    (jogador == "tesoura" and computador == "papel"):
                            print("Jogador ganhou a rodada!")
                            print(sep)
                            jogpoint += 1
                            break
                    else:
                        print('O computador venceu a rodada.')
                        print(sep)
                        comppoint+=1
                        break                    
            except ValueError:
                print('Informe sua escolha corretamente')
        n+=1
        
    geral= ganhadorgeral(jogpoint,comppoint)
    return geral