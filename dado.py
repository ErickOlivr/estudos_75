import random

jogadores = {'jogador1': random.randint(1,6),
             'jogador2': random.randint(1,6),
             'jogador3': random.randint(1,6),
             'jogador4': random.randint(1,6)}
for k, v in jogadores.items():
    print(k, ":", v)
