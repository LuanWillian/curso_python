from random import randint
from time import sleep
computador = randint(0, 5)

print('-=-'*20)
print('Pensei em um numero....')
print('-=-'*20)

usuario = int(input('Digite o numero que eu pensei: '))
print('PROCESSANDO....')
sleep(3)

if computador == usuario:
    print('Voce venceu!! Escolhi {} e voce {}'.format(computador, usuario))
    
else:
    print('Computador venceu!! Escolhi {} e voce {}'.format(computador, usuario))
