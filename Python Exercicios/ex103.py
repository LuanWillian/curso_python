def ficha(nome, gols):
    return f'O jogador {nome} fez {gols} gols no campeonato'


nome = str(input('Nome do jogador: ')).strip()
if nome == '':
    nome = '<Desconhecido>'
gols = str(input('Numeros de gols: ')).strip()
if gols.isnumeric() is False:
    gols = '0'
print(ficha(nome, gols))