somaidade = 0
maioridade = 0
maioridadehomem = 0
nomevelho = ''
totalmulher20 = 0
for p in range(1, 5):
    print('---- {}ª PESSOA ----'.format(p))
    nome = str(input('Nome: ')).capitalize()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: '))

    somaidade = somaidade + idade / 4

    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome

    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome

    if sexo in 'Ff' and idade < 20:
        totalmulher20 = totalmulher20 +1

print('A media de idades do grupo e de {}'.format(somaidade))
print('O homem mais velho tem {} anos e se chama {}'.format(maioridadehomem, nomevelho))
print('Ao todo são {} mulhere com menos de 20 anos'.format(totalmulher20))
