numero = []
while True:
    n = (int(input('Digite um numero: ')))
    if n not in numero:
        numero.append(n)
        print('Numero adicionado com sucesso!')
    else:
        print('Numero duplicado, nao vou adicionar')
    usuario = str(input('Quer continuar? [S/N]: ')).upper()[0].strip()
    while usuario not in 'SN':
        usuario = str(input('Quer continuar? [S/N]: ')).upper()[0].strip()
    if usuario == 'N':
        print(sorted(numero))
        break
