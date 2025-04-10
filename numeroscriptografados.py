def fibonacci(r):
    a, b = 0, 1
    for i in range(r): 
        a, b = b, a + b
    return a
    
def assinatura_dos_deuses(n: int):
    entrada=[]
    inteiros=[]
    senha=[]
    senha_final=""

    nmr=str(n)

    entrada =list(nmr)

    for e in entrada:
        inteiros.append(int(str(e)[::-1]))
    
    for c in inteiros:
        if c%2==0:
            senha.append(bin(c)[2:])
        elif c!=0:
            senha.append(str(fibonacci(c))[::-1])
    
    senha_final="".join(senha)
    
    return senha_final
    
while True:
    try:
        login = int(input("Insira sua senha para receber sua assinatura: "))
        break
    except:
        print("Porfavor informe sua senha com apenas numeros inteiros, sem espaço.")
        
print(f"Sua assinatura é: {assinatura_dos_deuses(login)}")