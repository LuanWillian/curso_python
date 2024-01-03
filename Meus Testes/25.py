numeros = []
maior = 0
menor = 0
cc = 0
for c in range(0, 6):
    numeros.append(int(input('Digite um numero: ')))
    if c == 0:
        maior = numeros[c]
        menor = numeros[c]
    else:
        if numeros[c] > maior:
            maior = numeros[c]
        if numeros[c] < menor:
            menor = numeros[c]
print(f'\nO maior numero e {maior} nas posições ', end='')
for en1, d in enumerate(numeros):
    if d == maior:
        print(f'{en1}... ', end='')

print('')
print(f'\nO menor numero e {menor} na posição ', end='')
for en2, e in enumerate(numeros):
    if e == menor:
        print(f'{en2}... ', end='')
