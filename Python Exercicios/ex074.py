from random import randint
maior = 0
menor = 0
junção = (randint(1,9), randint(1,9), randint(1,9), randint(1,9), randint(1,9))
print(f'Os numeros sorteados foram: ',end='')

for c in junção:
    print(f'{c} ',end='')

    '''if c == 0:
        maior = junção[0]
        menor = junção[0]
    else:
        if junção[1] > maior:
            maior = junção[1]
        if junção[1] < menor:
            menor = junção[1]
        if junção[2] > maior:
            maior = junção[2]
        if junção[2] < menor:
            menor = junção[2]
        if junção[3] > maior:
            maior = junção[3]
        if junção[3] < menor:
            menor = junção[3]'''

print('')
print(f'O maior numero e {max(junção)}')
print(f'O menor numero e {min(junção)}')