def fatorial(numero, show=False):
    """
    Esse programa faz o calculo de Fatorial
    param numero: Pega o valor
    param show=false: Da a condição se mostra o calculo ou não
    retunr: O fatorial de numero
    """
    mult = 1
    for c in range(numero, 0, -1):
        mult *= c
        if show is True:
            print(f'{c} x ', end='')
            if c == 2:
                print('1 = ', end='')
                break
    return mult


print(fatorial(5, True))
help(fatorial)
