def voto (i=0):
    idade = 2025 - i
    print(f"Você tem {idade} anos.", end=" ")
    if idade < 16:
        return "Voto negado"
    elif idade >=16 and idade > 65:
        return "Voto opcional"
    elif idade >= 18 and idade <= 65:
        return "Voto obrigatorio"

ano = int(input("Digite o ano que nasceu: "))
print(voto(ano))