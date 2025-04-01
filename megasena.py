import random
numero_sort = []
numero_int = range(0,99999)
numeros_str = [str(num) for num in numero_int]

jogos = input("Informe quantos jogos quer fazer: ")
while True:
    if jogos not in numeros_str:
        print("Digite corretamente.")
    else:
        jogos = int(jogos)
        break
for n in range(1,jogos+1):
    for i in range(0,6):
            numero_sort.append(random.randint(1, 61))
    print(f"Seu {n}° jogo: {numero_sort}")
    numero_sort.clear()

    
