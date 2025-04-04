def ficha (jog="desconhecido", nmr=0): 
    print(f"O jogador {jog} marcou {nmr} gols.")


jog = input("insira o nome do jogador: ")
gol = (input("Quantos gols o jogador(a) fez: "))
ficha(jog,gol)
if gol.isnumeric:
    gol=int(gol)
else: 
    gol = 0

if jog.strip()== "":
    ficha(nmr=gol)
else:
    ficha(jog,gol)
