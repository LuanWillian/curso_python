
def validarCartao(n):
    """ Faz a validação do numero do cartão

    Args:
        n (str): Pega o numero pra fazer a validação
    """
    lista = []
    for c in n:
        lista.append(c)
    if len(lista) != 13:
        while len(lista) != 13:
            print('ERRO! numero do cartão ou codigo CVV invalido! Tente novamnete!')
            lista.clear()
            cartao = str(input('Digite o numero do cartão: '))
            for c in cartao:
                lista.append(c)


def validarCvv(n):
    """ Faz a validação do codigo CVV

    Args:
        n (str): Pega o numero pra fazer a validação
    """
    lista = []
    for c in n:
        lista.append(c)
    if len(lista) != 3:
        while len(lista) != 3:
            lista.clear()
            cvv = str(input('Digite o CVV do cartão: '))
            for c in cvv:
                lista.append(c)
    print('Cartao cadastrado')
