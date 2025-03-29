clientes = []
for p in range(0,2):
    pessoas = []  
    pessoas.append(input("Digite o nome do cliente: "))
    pessoas.append(int(input("Digite a idade do cliente: ")))
    clientes.append(pessoas)
for n in clientes:
    print(f"{n[0]} tem {n[1]} anos de idade.")
    if n[1] >= 21:
        print(f"{n[0]} é maior de idade")
    else:
        print(print(f"{n[0]} é menor de idade"))