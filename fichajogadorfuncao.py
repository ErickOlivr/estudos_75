def ficha (jog=0, nmr=0):
    if jog == 0:
        jog = "Desconhecido"
    print(f"O jogador {jog} marcou {nmr} gols.")




jog = input("insira o nome do jogador: ")
gol = (input("Quantos gols o jogador(a) fez: "))
ficha(jog,gol)

