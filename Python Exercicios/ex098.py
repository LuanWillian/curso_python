from time import sleep


def contador(i, f, p):
    if p < 0:
        p *= -1

    if p == 0:
        p = 1
    print('-='*20)
    print(f'Contagem de {i} ate {f} de {p} em {p}')

    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont}', end=' ', flush=True)
            sleep(1)
            cont += p
        print('FIM!')
    else:
        cont = i
        while cont >= f:
            print(f'{cont}', end=' ', flush=True)
            sleep(1)
            cont -= p
        print('FIM!')


contador(1, 10, 1)
contador(10, 0, 2)
inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio, fim, passo)
