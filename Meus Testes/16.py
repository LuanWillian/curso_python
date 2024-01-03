maior = 0
menor = 0
for x in range(1,3):
    a = int(input('Digite um numero: '))
    if x == 1:
        maior = a
        menor = a
    if a > maior:
        maior = a
    if a < menor:
        menor = a
print('O maior e {}'.format(maior))
print('O menor {}'.format(menor))

