numero = []
c = 0
while c < 2:
    i = int(input("Digite um numero menor que 10"))
    if i < 10:
        numero.append(i)
        c = c + 1
    else:
        print("digite um numero menor que 10")
print(numero[0] + numero[1])


