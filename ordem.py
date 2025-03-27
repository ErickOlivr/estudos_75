inteiros = range(0,99999)
inteiros_str = [str(num) for num in inteiros]
nmr = []
continuar = ("sim", "não")
print("vasco")
while True:
    while True:
        i = (input("Digite um numero: "))
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
         nmr.sort
         print(nmr)
         break
    elif cont == "sim":
         print("continuando...")

                


    