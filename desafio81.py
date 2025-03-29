inteiros = range(0,99999)
inteiros_str = [str(num) for num in inteiros]
nmr = []
continuar = ("sim", "não")

while True:
    while True:
        i = (input("Digite um numero de 0 até 99999: "))
        if i in inteiros_str:
            i = int(i)
            if not i in nmr:
                nmr.append(i)
                break
            else:
                print("Valor já inserido, por favor digite outro numero")
        else:
            print("Digite um numero inteiro.")
    
    while True:
        cont = input("Deseja continuar?(sim/não) ").strip().lower()
        if not cont in continuar:
            print("Digite corretamente")
        else:
            break 
            
    if cont == "não":
         len(nmr)
         nmr.sort(reverse=True)
         print(nmr)
         if 5 in nmr:
             print("O número 5 foi inserido")
         else:
             print("O número 5 não foi inserido")
         break
    elif cont == "sim":
         print("continuando...")
