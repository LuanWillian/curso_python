lista = []
while True:
    lista.append(int(input('Digite um numero: ')))
    usuario = str(input('Quer continuar? [S/N]: ')).upper()[0].strip()
    while not usuario in 'SN':
        usuario = str(input('Quer continuar? [S/N]: ')).upper()[0].strip()

    if usuario == 'N':
        lista.sort(reverse=True)
        print(f'Você digitou {len(lista)} elementos!')
        print(f'Os valores em ordem decrecente são: {lista}')
        if 5 in lista:
            print('O valor 5 faz parte da lista!')
        else:
            print('O valor 5 não faz parte da lista!')
        break
