soma = 0
n = 0
for c in range(1, 6):
    nmr = int(input("digite um numero"))
    if nmr%2 == 0:
        soma = nmr + n
        n = soma
print(soma)