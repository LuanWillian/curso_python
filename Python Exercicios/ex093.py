dados = dict()
lista = []
soma = 0
dados['Nome'] = str(input('Nome: '))
dados['Partidas'] = int(input('Partidas jogadas: '))
for c in range(0, dados['Partidas']):
    lista.append(int(input(f'Quantos gols na partida {c}? ')))
    soma += lista[c]
    if c+1 == dados['Partidas']:
        dados['Gols'] = lista
        dados['Total'] = soma
print('*'*48)
for k, v in dados.items():
    print(f'{k} tem o valor {v}')
print('*'*48)
print(f'O jogador {dados["Nome"]} Jogou {dados["Partidas"]} partidas')
for c in range(0, dados['Partidas']):
    print(f'Na partida {c}, fez {lista[c]}')
print(f'Foi um total de {soma} gols.')
