def leiadinheiro():
    while True:
        try:
            d = str(input('Digite o preço: R$')).replace(',', '.').strip()
            if d.isalpha():
                print('ERRO, DIGITE UM NUMERO VALIDO')
            else:
                d = float(d)
                break
        except ValueError:
            print('Digite corretamente.')
    return d


def leiaporcent():
    while True:
        try:
            p = int(input('Informe a porcentagem de 0 a 100%: (ex: 100, 40, 24...)'))
            if p >=0 and p <=100:
                p /=100
                break
        except ValueError:
            print('Digite corretamente.')
    return p