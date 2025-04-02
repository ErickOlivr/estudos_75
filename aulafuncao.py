def conta():
    for n in range(0,2):
        while True:
            try:
                nmr = int(input("digite um numero: "))
                print(nmr)
                break
            except ValueError:
                print("digite corretamente um numero inteiro")
    

conta()

