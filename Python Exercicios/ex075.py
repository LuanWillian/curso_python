junção = (int(input('Digite o primeiro numero: ')),
          int(input('Agora o segundo numero: ')),
          int(input('Agora o terceiro numero: ')),
          int(input('O ultimo numero: ')))

print(f'Voce digitou os numeros: {junção}')
print(f'O numero 9 apareceu {junção.count(9)} vezes!')

if 3 in junção:
    print(f'O numero 3 apareceu na {junção.index(3)+1}ª posição!')
else:
    print('O numero 3 não foi digitado em nenhuma posição!')
print(f'Os numeros pares digitados foram: ',end='')

for c in junção:
    print(c)
    if c % 2 == 0:
        print(c)
