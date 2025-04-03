def contador(i,f,p):
    if p < 0:
        p*=-1
    if p == 0:
        p ==1

    print(f"Contagem de {i} até {f} de {p} em {p}")
    
    if i < f:
        cont = i
        while cont <= f:
            print(f"{cont} ", end="")
            cont += p
        print("Fim")
    else:
        cont = i
        while cont >=f:
            print(f"{cont} ", end="")
            cont -= p
        print("fim")


contador(1,10,1)
contador(10,0,2)
print("Agora é sua vez de personalizar a contagem! ")
ini = int(input("inicio: "))
fim = int(input("fim: "))
pas = int(input("pas: "))
contador(ini,fim,pas)
