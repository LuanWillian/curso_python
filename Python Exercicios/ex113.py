def leiaint(m):
    valor = 0
    while True:
        try:
            valor = int(input(m))
            break
        except ValueError:
            print('\033[0;31mERRO! Digite um numero inteiro valido.\033[m')
        except KeyboardInterrupt:
            print('\n\033[0;31mEntrada de dados interrompida pelo usuario!\033[m')
            break
    return valor


def leiafloat(f):
    valor = 0
    while True:
        try:
            valor = float(input(f))
            break
        except ValueError:
            print('\033[0;31mERRO! Digite um numero inteiro valido.\033[m')
        except KeyboardInterrupt:
            print('\n\033[0;31mUsuario preferio não digitar um valor!\033[m')
            break
    return valor

inteiro = leiaint('Digite um numero Inteiro: ')
real = leiafloat('Digite um numero Real: ')
print(f'O valor inteiro digitado foi {inteiro} o valor real foi {real}')
