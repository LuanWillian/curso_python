def metade(numero):
    m = numero / 2
    return m


def dobro(numero):
    d = numero * 2
    return d


def aumentar(numero, porc):
    a = numero + numero * porc / 100
    return a


def diminuir(numero, porc):
    d = numero - numero * porc / 100
    return d


def moeda(numero=0, moeda='R$'):
    return f'{moeda}{numero:.2f}'.replace('.', ',')
