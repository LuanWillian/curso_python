dados = dict()
gols = []
jogadores = []
soma = 0
while True:
    dados['Nome'] = str(input('Nome: '))
    dados['Partidas'] = int(input('Partidas jogadas: '))
    for c in range(0, dados['Partidas']):
        gols.append(int(input(f'Quantos gols na partida {c}? ')))
        soma += gols[c]
    dados['Gols'] = gols[:]
    gols.clear()
    dados['SomaGols'] = soma
    soma = 0
    jogadores.append(dados.copy())
    usuario = str(input('Quer continuar?[S/N]: ')).upper()[0]

    if usuario == 'N':
        print('-'*30)
        for p, c in enumerate(jogadores):
            print(f'{p} {c["Nome"]}    {c["Gols"]}   {c["SomaGols"]}')
        print('-'*30)
        while True:
            usuario = int(input('Ver dados de qual jogador?: '))
            if usuario == '999':
                break
            if usuario > len(jogadores):
                print(f'ERRO! Não existe jogador com codigo {usuario}')
            if usuario < len(jogadores):
                print(f'VER DADOS DO JOGADOR {jogadores[usuario]["Nome"]}')
                for p, c in enumerate(jogadores[usuario]['Gols']):
                    print(f'No jogo {p} fez {c}')
