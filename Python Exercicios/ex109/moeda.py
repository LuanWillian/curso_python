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
