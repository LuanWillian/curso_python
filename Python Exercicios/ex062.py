print('')
print('Gerenciador de PA')
print('')
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razao da PA: '))
termo = primeiro
cont = 0
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont < total:
        cont = cont +1
        print('{} -> '.format(termo),end='')
        termo = termo + razao
    print('Pausa')
    mais = int(input('Quantos termos voce quer colocar a mais? '))
print('Progressão finalizada {} termos mostrados'.format(total))