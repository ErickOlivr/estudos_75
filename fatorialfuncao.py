def fatorial(show,num=1):
    f = 1
    for c in range(num, 0, -1):
        if show == "sim":
            print(c, end="")
            if c > 1:
                print(" x ", end="")
            else:
                print(" = ", end="")
        f *= c    
    return (f)


mostra = ("sim", "não")
nmr = 0
while True:
    try:
        nmr = int(input("Digite um numero que deseja fatorar: "))
        break
    except ValueError:
        print("digite um numero inteiro.")

while True:
    try:
        resp = (input("Deseja que mostre o processo de fatoração? (sim/não)")).strip().lower()
        if resp in mostra:
           break
        else:
            print("digite corretamente")
    except ValueError:
        print("Digite corretamente")

print(fatorial(resp,nmr))


