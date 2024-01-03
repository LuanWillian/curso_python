from datetime import date
atual = date.today().year
ano = int(input('Qual ano voce nasceu?: '))
idade = atual - ano

print('O aleta tem {} anos'.format(idade))

if idade <= 9:
    print('Voce e MIRIM!')

elif idade <= 14:
    print('Voce e INFANTIL!')

elif idade <= 19:
    print('Voce e JUNIOR')

elif idade <= 25:
    print('Voce e SENIOR!')

elif idade > 25:
    print('Voce e MASTER!')