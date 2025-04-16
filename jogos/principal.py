from games import advinhacao,ppt,jogodavelha
import textos
p = 0
cont=1
ordem =[]
print(textos.explicacao)
print(textos.comeco)
while True:
    while cont < 4:
        while True:
            try:
                escolha=int(input('Escolha a ordem dos jogos: '))
                if escolha >=1 and escolha <= 3:
                    if escolha not in ordem:
                        ordem.append(escolha)
                        break
                    else:
                        print('Já foi escolhido seu arrombado, digita oto ai')
                else:
                    print('Fi de rapariga, informe um numero entre 3, 2, 1.')
            except ValueError:
                print('Use os numeros como forma de selecionar os jogos.')
        cont+=1
    
    for jogo in ordem:
        if jogo == 1:
            p += advinhacao.advinhacao()
        elif jogo == 2:
            p += jogodavelha.jogodavelha()
        else:
            p += ppt.ppt()
    
    if p >= 5:
        print(f'Você fez {p} pontos! Parabens pela vitoria.')
    elif p < 5:
        print(f'Você fez {p} pontos! Parabens pela derrota, seu fracassado.')
    
    while True:
        try:
            continua = str(input('Gostaria de participar dos jogos vuc vuc novamente?(sim/não)')).strip().lower()
            if continua in ('sim', 'não'):
                break     
        except ValueError:
            print('Digite corretamente uma das opções')
            
        if continua == 'não':
            print('Obrigado por jogar.')
            break
        elif continua == 'sim':
            print('continuando...')