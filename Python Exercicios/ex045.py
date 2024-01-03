from random import randint
from time import sleep

itens = ('PEDRA', 'PAPEL', 'TESOURA')
computador = randint(0,2)
print('''Qual a sua jogada?
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura''')
jogador = int(input('Sua Jogada: '))

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!')
sleep(1)

print('=-' * 12)
print('Computador jogou {}'.format(itens[computador] ))
print('O jogador jogou {}'.format(itens[jogador]))
print('=-' * 12)

if computador == 0: # Computador jogou PEDRA

    if jogador == 0:
        print('EMPATE!')
    elif jogador == 1:
        print('VOCE VENCEU!')
    elif jogador == 2:
        print('COMPUTADOR VENCEU!')
    else:
        print('Opção invalida!')

elif computador == 1: # Computador jogou PAPEL

    if jogador == 0:
        print('COMPUTADOR VENCEU!')
    elif jogador == 1:
        print('EMPATE!')
    elif jogador == 2:
        print('VOCE VENCEU!')
    else:
        print('Opção invalida!')

elif computador == 2: # Computador jogou TESOURA
    
    if jogador == 0:
        print('VOCE VENCEU!')
    elif jogador == 1:
        print('COMPUTADOR VENCEU!')
    elif jogador == 2:
        print('EMPATE!')
    else:
        print('Opção invalida!')
