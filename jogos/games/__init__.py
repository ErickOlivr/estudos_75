def ganhadorgeral(j,c):
    jog = j
    comp = c
    if jog == comp:
        print('Empate.')
        return 1
    elif jog < comp:
        print(f'O computador ganhou de {comp} a {jog}')
        return -2
    else:
        print(f'Jogador ganhou de {jog} a {comp}')
        return 3