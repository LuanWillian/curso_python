real = float(input('Digite seu saldo em R$: '))
dolar = real / 4.86
euro = real / 5.26
yuan = real / 0.68
ruplo = real / 0.058
chileno = real / 164.59
print('Seu saldo em R$ da pra comprar US$: {:.2f}.'.format(dolar))
print('Seu saldo em R$ da pra comprar €: {:.2f}'.format(euro))
print('Sue saldo em R$ da pra comprar ¥: {:.2f}'.format(yuan))
print('Seu saldo em R$ da pra comprar ₽: {:.2f}'.format(ruplo))
print('Seu saldo em R$ da pra comprar $: {:.2f}'.format(chileno))