from datetime import date
menoridade = 0
maioridade = 0

for c in range(1,8):
    nascimento = int(input('Qual ano a {}ª pessoa nasceu? '.format(c)))
    ano = date.today().year
    idade = ano - nascimento

    if idade < 18:
        menoridade = menoridade + 1
    else:
        maioridade = maioridade + 1

print('''Ao todo tivemos {} pessoa maiores de idade
E tambem tivemos {} pessoas menores de idade '''.format(maioridade, menoridade))
