from random import randint
jogador = 0
contador = 0
computador = randint(0,10)
while not computador == jogador:
    jogador = int(input('Digite um numero: '))
    contador = contador +1
    if computador == jogador:
        print('')
        print('Você palpitou {} vezes'.format(contador,computador))
        print('O computador jogou o numero {}'.format(computador))
        print('E voce Jogou o numero {}'.format(jogador))
        print('')
    elif computador > jogador:
        print('MAIS... TENTE NOVAMENTE')
    elif computador < jogador:
        print('MENOS... TENTE NOVAMENTE')