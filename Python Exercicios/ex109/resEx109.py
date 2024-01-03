import moeda

preço = float(input('Digite o preço R$'))
print(f'A metade de {moeda.moeda(preço)} e {moeda.metade(preço, True)}')
print(f'O dobro de {moeda.moeda(preço)} e {moeda.dobro(preço, True)}')
print(f'Aumentando 10%, temos {moeda.aumentar(preço, 10, True)}')
print(f'Reduzindo 13%, temos {moeda.diminuir(preço, 13, True)}')
