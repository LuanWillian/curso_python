lista = list()
juntar = list()
pesado = 0
leve = 0
nomePesado = ''
nomeLeve = ''
while True:
    juntar.append(str(input('Digite seu nome: ')))
    juntar.append(int(input('Digite seu peso Kg')))
    usuario = str(input('Quer continuar [S/N]: ')).upper()[0].strip()
    lista.append(juntar[:])
    juntar.clear()

    if usuario == 'N':
        print(f'Ao todo, você cadatrou {len(lista)} pessoas!')
        for c in range(0,len(lista)):
            if c == 0:
                pesado = lista[c][1]
                nomePesado = lista[c][0]
                leve = lista[c][1]
                nomeLeve = lista[c][0]
            else:
                if pesado < lista[c][1]:
                    pesado = lista[c][1]
                    nomePesado = lista[c][0]
                if leve > lista[c][1]:
                    leve = lista[c][1]
                    nomeLeve = lista[c][0]
        print(f'O maior peso foi de {pesado}Kg. poso de {nomePesado}')
        print(f'O menor peso foi de {leve}Kg. peso de {nomeLeve}')
        break
