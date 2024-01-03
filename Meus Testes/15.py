mediaidade = 0
idadehomemvelho = 0
homemvelho = ''
mulhermaisnova = 0
for dados in range (1,5):
    print('---- Dados da {}ª pessoa----'.format(dados))
    nome = str(input('Digite seu nome: ')).strip().capitalize()
    idade = int(input('Digite sua idade: '))
    sexo = str(input('Seu sexo [M/F]: '))
    mediaidade = mediaidade + idade / 4
    if dados == 1 and sexo in 'Mm':
        idadehomemvelho = idade
        homemvelho = nome
    if sexo in 'Mm' and idade > idadehomemvelho:
        idadehomemvelho = idade
        homemvelho = nome
    if sexo in 'Ff' and idade < 20:
        mulhermaisnova = mulhermaisnova + 1

print('A media do grupo e {}'.format(mediaidade))
print('o Homem mais velho tem {} anos e se chama {} !'.format(idadehomemvelho, homemvelho))
print('Tem {} mulheres com menos de 20 anos!'.format(mulhermaisnova))
