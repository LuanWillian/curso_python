maior = 0
nome2 = ''
for pessoas in range(1,4):
    print('--- Ola ---')
    nome = str(input('Qual seu nome: ')).capitalize()
    salario = float(input('Qual seu salario R$'))
    
    if pessoas == 1:
        maior = salario
        nome2 = nome

    else:
        if salario > maior:
            maior = salario
            nome2 = nome

print('O maior salario e {} e pertence a {}'.format(maior,nome2))