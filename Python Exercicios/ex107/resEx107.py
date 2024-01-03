import moeda

preço = float(input('Digite o preço R$'))
print(f'A metade de {preço} e {moeda.metade(preço)}')
print(f'O dobro de {preço} e {moeda.dobro(preço)}')
print(f'Aumentando 10%, temos {moeda.aumentar(preço, 10)}')
print(f'Reduzindo 13%, temos {moeda.diminuir(preço, 13)}')
