def leiaint(m):
    """
    Esse programa faz a validação se um numero e inteiro ou não
    param m: Pega o numero que o usuario digitou
    return: Retorna um valor inteiro
    """
    while True:
        valor = str(input(m))
        if valor.isnumeric():
            m = int(valor)
            break
        else:
            print('\033[0;31mERRO! Digite um numero inteiro valido.\033[m')
    return m


numero = leiaint('Digite um numero: ')
print(f'Voce digitou o numero {numero}')
help(leiaint)
