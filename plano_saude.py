nome = input("digite seu nome: ")
idade = int(input("Digite sua idade: "))
if idade <= 10:
    print("Pagará 130 reais")
elif idade >= 10 and idade <= 29:
    print("Pagará 160 reais")
elif idade >= 29 and idade <= 45:
    print("Pagará 220 reais")
elif idade >= 45 and idade <= 59:
    print("Pagará 250 reais")
elif idade >= 59 and idade <= 65:
    print("Pagará 350 reais")
else:
    print("Pagará 600 reais")