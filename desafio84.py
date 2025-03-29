clientes = []
pessoas = []
inteiros = range(0,99999)
inteiros_str = [str(num) for num in inteiros]
continuar = ("sim", "não")

while True:
    while True:
        leve = []
        pesado = []
        pessoas.append(input("Digite o nome do cliente: "))
        pessoas.append(int(input("Digite o peso do cliente: ")))
        
        clientes.append(pessoas[:])
        pessoas.clear()
        break

    while True:
        pergunta = input("Deseja continuar?(sim/não) ").strip().lower()
        if not pergunta in continuar:
            print("Digite corretamente")
        else:
            break 

    if pergunta == "não":
        clientes_ord = sorted(clientes, key=lambda x: x[1], reverse = True)

        max_peso = max(cliente[1] for cliente in clientes)
        
        min_peso = min(cliente[1] for cliente in clientes)

        pesado = [cliente[0] for cliente in clientes_ord if cliente[1] == max_peso]
        leve = [cliente[0] for cliente in clientes_ord if cliente[1] == min_peso]

        print(f"O/os clientes mais pesados é/são: {', '.join(pesado)} ({max_peso} kg)")
        print(f"O/os clientes mais leves é/são: {', '.join(leve)} ({min_peso} kg)")
        break
    else:
            print("continuando")