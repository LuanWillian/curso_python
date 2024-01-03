from random import choice
print('=' * 20)
print('BOA SORTE A TODOS!!!')
print('=' * 20)

n1 = input('Digite o nome do candidato: ')
n2 = input('Digite o nome do candidato: ')
n3 = input('Digite o nome do candidato: ')
n4 = input('Digite o nome do candidato: ')
n5 = input('DIgite o nome do candidato: ')
n6 = input('Digite o nome do candidato: ')

candidatos = [n1, n2, n3, n4, n5, n6]
premiado = choice(candidatos)

print('PARABENS {}!!!!! GANHOU R$1.000.000.00'.format(premiado))