numero = []
maior = 0
menor = 0
for c in range(0,5):
    numero.append(int(input('Digite um numero: ')))
    if c == 0:
        maior = numero[c]
        menor = numero[c]
    else:
        if maior < numero[c]:
            maior = numero[c]
        if menor > numero[c]:
            menor = numero[c]
print(f'O maior numero foi {maior} nas posiçoes: ',end='')
for p, d in enumerate(numero):
    if d == maior:
     print(f'{p}...')
print(f'O menor numero foi {menor} nas posiçoes: ',end='')
for p1,e in enumerate(numero):
    if e == menor:
        print(f'{p1}...')