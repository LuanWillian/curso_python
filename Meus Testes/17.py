maior = 0
menor = 0
contador = 0
for ale in range(1, 4):
    vl = int(input('Digite um valor: '))
    while vl < 5:
        print('Tente Novamente!')
        vl = int(input('Digite um valor: '))
        contador = contador + 1
    if ale == 1:
        maior = vl
        menor = vl
    else:
        if vl > maior:
            maior = vl
        if vl < menor:
            menor = vl
print('O maior numero  e {} e o menor e {}'.format(maior,menor))
print('Voce errou {} vezes'.format(contador))
