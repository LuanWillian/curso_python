from random import randint
from time import sleep
contador = 0
while True:
    computador = randint(1,10)
    jogador = int(input('Digite um valor: '))
    opção = str(input('Par ou Inpar[P\I]: ')).strip().upper()[0]

    while not opção in 'PI':
        print('Ops, opção invalida! Tente Novamente!')
        opção = str(input('Par ou Inpar[P\I]: ')).strip().upper()[0]

    soma = jogador + computador
    resultado = soma % 2

    if resultado == 1 and opção == 'I':
        print('-'*53)
        print(f'Voce Jogou {jogador} e o computador {computador}. Total de {soma} deu INPAR!')
        print('-'*53)
        print('Voce VENCEU!')
        print('Vamos mais uma rodada...')
        print('-='*27)
        sleep(2)
        contador = contador+1

    elif resultado == 0 and opção == 'P':
        print('-'*53)
        print(F'Voce jogou {jogador} e o computador {computador}. Total de {soma} deu PAR! ')
        print('-'*53)
        print('Voce VENCEU!')
        print('Vamos mais uma rodada...')
        print('-='*27)
        sleep(2)
        contador = contador +1

    elif resultado == 1 and opção != 'I':
        print('-'*53)
        print(f'Voce jogou {jogador} e o computador {computador}. Total de {soma} deu INPAR!  ')
        print('-'*53)
        print('Voce PERDEU!')
        print('-='*27)
        print(f'GAME OVER Voce ganhou {contador} vezes')
        break

    elif resultado == 0 and opção != 'P':
        print('-'*53)
        print(f'Voce jogou {jogador} e o computador {computador}. Total de {soma} deu PAR!')
        print('-'*53)
        print('Voce PERDEU!')
        print('-='*27)
        print(f'GAME OVER! Voce ganhou {contador} vezes')
        break
