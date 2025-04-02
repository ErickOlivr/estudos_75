def area(lst):
    a = lst[0]*lst[1]
    print(f"A área do retangulo é de {a}m²")

lados = []
for n in range(1,3):
    while True:
        lado = (float(input(f"Digite o {n}° lado: ")))
        try:
            lados.append(lado)
            break
        except ValueError:
            print("Digite um numero real.")
area(lados)


        