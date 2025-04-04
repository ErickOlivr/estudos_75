par = 0
soma = 0
for c in range(1,7):
    while True:
        try:
            nmr = float(input(f"Digite o {c}° numero."))
            break
        except ValueError:
            print("Digite corretamente")

    soma += nmr
    if nmr%2==0:
        par += 1
media = soma/6
print(f"{par} numeros pares inseridos, a média dos numeros inseridos é {media:.2f} ")
