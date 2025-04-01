alunosemedia = []
resposta = ["sim", "não"]
while True:
    nota = []
    aluno = input("Digite o nome do aluno: ").strip()
    for n in range(1,3):
        while True:
            try:
                notas = float(input(f"Digite a {n}° nota do aluno: "))
                if notas >= 0 and notas <= 10:
                    nota.append(notas)
                    break
                else:
                    print("Digite nota entre 0 e 10.")
            except:
                print("Insira um numero decimal")

    media = (nota[0]+ nota[1])/2

    alunosemedia.append((aluno,media))

    while True:
        continua = input("Deseja inserir mais alunos?(sim/não)").lower().strip()
        if continua not in resposta:
            print("Digite corretamente: ")
        else:
            break

    if continua == "não":
        for nome, media in alunosemedia:
            print(f"{nome}: {media:.2f}")
        
        break
    else:
        print("...")