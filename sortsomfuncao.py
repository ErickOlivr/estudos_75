import random

def sorteia(list):
    print("Sorteando 5 numeros da lista: ", end="")
    for cont in range (0,5):
        n = random.randint(1,10)
        list.append(n)
        print(f"{n}",end=" ", flush=True)
    print()
        

def somapar(list):
    soma = 0
    for n in list:
        if n%2== 0:
            soma += n
    print(f"A soma entre {numeros} numeros é {soma}")


numeros=[]
sorteia(numeros)
somapar(numeros)
