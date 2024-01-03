def contador(i, f, p):
    """
    Faz uma contagem e mostra na tela
    :param i: Inicio da contagem
    :param f: Fim da contagem
    :param p: Passos da contagem
    :return: Sem retorno
    """
    c = i
    while c <= f:
        print(c, end='..')
        c += p
    print('Fim!')


contador(0, 20, 2)


help(contador)