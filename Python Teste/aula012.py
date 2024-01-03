nome = str(input('Digite seu nome: ')).upper()

if nome == 'LUAN':
    print('Seu nome e tao lindo!')

elif nome == 'PEDRO' or nome == 'MARIA' or nome == 'PAULO':
    print('Seu nome e muito popular no Brasil!')

elif nome in 'ANA CLAUDIA JESICA JULIANA':
    print('Belo nome feminino')

print('Tenha um Bom Dia {}!'.format(nome.title()))