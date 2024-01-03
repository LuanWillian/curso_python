lista = []
contador = 0
soma = 0
while True:
    nome = str(input('Nome: '))
    sexo = str(input('Sexo: '))
    while sexo not in 'MmFf':
        print('ERRO Digite apenas M ou F')
        sexo = str(input('Sexo: '))
    idade = int(input('idade: '))
    dados = {'Nome': nome, 'Sexo': sexo, 'Idade': idade}
    lista.append(dados.copy())
    contador += 1
    usuario = str(input('Quer continuar?[S/N]: '))
    while usuario not in 'SsNn':
        print('ERRO Digite apenas S ou N')
        usuario = str(input('Quer continuar?[S/N]: '))
    if usuario in 'Nn':
        for c in lista:
            if c['Idade'] >= 0:
                soma += c['Idade']
        media = soma / contador
        mulheres = []
        for c in lista:
            if c['Sexo'] in 'Ff':
                mulheres.append(c['Nome'])
        print(f'O grupo tem {contador} Pessoas')
        print(f'A media de idade e {media} anos')
        print(f'As mulheres cadastradas foram: {mulheres}')
        acimaMedia = []
        for c in lista:
            if c['Idade'] >= media:
                acimaMedia.append(c['Nome'])
        print(f'Pessoa com idade acima da media foi: {acimaMedia}')
        break
