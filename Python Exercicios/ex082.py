lista = list()
par = list()
impar = list()
while True:
    lista.append(int(input('Digite um numero: ')))
    usuario = str(input('Quer continuar? [S/N]: ')).upper()[0].strip()
    while not usuario in 'SN':
        usuario = str(input('Quer continuar? [S/N]: ')).upper()[0].strip()

    if usuario == 'N':
        print(f'A lista completa e {lista}')
        for c in lista:
            if c % 2 == 0:
                par.append(c)
            else:
                impar.append(c)
        print(f'A lista de pares e {par}')
        print(f'A lista de impar e {impar}')
        break