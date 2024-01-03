from time import sleep
from random import randint
numeros = []


def sorteio(lista):
    print('Sorteando 5 valores da lista: ', end='')
    for c in range(1, 6):
        sorteioNum = randint(1, 10)
        lista.append(sorteioNum)
        print(sorteioNum, end=' ', flush=True)
        sleep(0.5)


def somaPar(lista):
    print()
    soma = 0
    for c in lista:
        if c % 2 == 0:
            soma += c
    print(f'Somando os valores pares de {lista}, temos {soma}')


sorteio(numeros)
somaPar(numeros)
