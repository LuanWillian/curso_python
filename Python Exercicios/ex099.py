from random import randint
from time import sleep


def maior(*numeros):
    maior = 0
    tamanho = len(numeros)
    for c in range(0, tamanho):
        if c == 0:
            maior = numeros[c]
        else:
            if maior < numeros[c]:
                maior = numeros[c]
    print('Analisando os valores pasados...', flush=True)
    sleep(1.5)
    for c in numeros:
        print(c, end=' ', flush=True)
        sleep(0.2)
    print(f' Foram informados {tamanho} valores ao todo.')
    print(f'O Maior valor informado foi {maior}')
    print()


maior(randint(1, 9), randint(1, 9), randint(1, 9), randint(1, 9))
maior(randint(1, 9), randint(1, 9), randint(1, 9))
maior(randint(1, 9), randint(1, 9))
maior(randint(1, 9))
maior(0)
