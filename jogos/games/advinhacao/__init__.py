def advinhacao():
    import random,textos
    from games import ganhadorgeral
    sep = '-'*40
    jog= 0
    comp=0
    p = 1
    print(textos.exp_advinhacao)
    print()
    while p < 4:
        print(f'Rodada {p} de 3.')
        numero_secreto = random.randint(0,101)
        cont = 7
        while cont > 0:
            pergunta = (f"Você tem apenas {cont} chances, digite um número de 0 a 100: ")
            while True:
                try:
                    numero = int(input(pergunta))
                    if 0 <= numero <= 100:
                        if numero == numero_secreto:
                            print("O jogador ganhou a rodada!!!!!!!!")
                            print(sep)
                            jog += 1
                            cont-=7
                            break
                        elif numero > numero_secreto:
                            print("O numero mistérioso é menor")
                            print()
                            cont += -1
                        else:
                            print("o numero mistérioso é maior")
                            print()
                            cont += -1
                        break
                    else:
                        print("Digite um numero entre 0 e 100")
                        print()
                except ValueError:
                    print("Digite um número entre 0 e 100, porfavor")
                    print()
    
        if cont == 0:
            print(f"""O computador venceu a rodada!!!!
O numero secreto era: {numero_secreto} """)
            print(sep)
            comp += 1
        p+=1
                   
    print('Obrigador por jogar Advinhação!!!')
    geral = ganhadorgeral(jog,comp)
    return geral