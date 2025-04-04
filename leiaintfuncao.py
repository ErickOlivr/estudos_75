def leiaint(nmr):
    while True:
        try:
            n = int(input(nmr))
            return n
        except ValueError:
            print("ERRO")


nmr = leiaint("Digite um numero inteiro: ")
print(nmr)


