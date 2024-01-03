def metade(numero, f=False):
    m = numero / 2
    if f:
        i = moeda(m)
        m = i
    return m


def dobro(numero, f=False):
    d = numero * 2
    if f:
        i = moeda(d)
        d = i
    return d


def aumentar(numero, porc, f=False):
    a = numero + numero * porc / 100
    if f:
        i = moeda(a)
        a = i
    return a


def diminuir(numero, porc, f=False):
    d = numero - numero * porc / 100
    if f:
        i = moeda(d)
        d = i
    return d


def moeda(numero=0, moeda='R$'):
    return f'{moeda}{numero:.2f}'.replace('.', ',')


def resumo(valor=0, porc1=0, porc2=0):
    print('-'*25)
    print('RESUMO DO VALOR'.center(25))
    print('-'*25)
    print(f'Preço analisado: \t{moeda(valor)}')
    print(f'Dobro do preço: \t{dobro(valor,True)}')
    print(f'Metade do preço: \t{metade(valor, True)}')
    print(f'{porc1}% de aumento: \t{aumentar(valor, porc1, True)}')
    print(f'{porc2}% de redução: \t{diminuir(valor, porc2, True)}')
