def metade(n):
    res=(n/2)
    return moeda(res)


def dobro(n):
    res = n*2
    return moeda(res)


def diminuindo(n,p):
    res = n-(n*p)
    return moeda(res)


def aumentando(n,p):
    res= n+(n*p)
    return moeda(res)


def moeda(n, moeda='R$'):
    return (f'{moeda}{n:.2f}'.replace('.',','))


def resumo (dinheiro, p):
    pontos = '-'*30
    print(f'''{pontos}
      RESUMO DO VALOR
{pontos}  
Valor analisado:   {moeda(dinheiro,)}      
Metade:            {metade(dinheiro)}
Dobro:             {dobro(dinheiro)}
Aumento de {p*100}%:  {aumentando(dinheiro,p)}
Redução de {p*100}%:  {diminuindo(dinheiro,p)}
{pontos}'''.replace('.', ','))