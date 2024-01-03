maior = 0
menor = 0
from datetime import date
for contador in range(1,8):
    nascimento = int(input('Digite o ano de nascimento da {}ª pessoa: '.format(contador)))
    ano = date.today().year
    idade = ano - nascimento

    if idade > 18:
        maior = maior +1
    else:
        menor = menor +1

print('Os dados fornecido acima tem {} pessoas maiores de idade'.format(maior))
print('Os dados fornecido acima tem {} pessoas menores de idade'.format(menor))
