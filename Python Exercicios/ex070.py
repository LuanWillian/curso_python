total = 0
cont1000 = 0
contador = 0
caro = 0
barato = 0
baratonome = ''
while True:
    nomeproduto = str(input('Nome do produto: ')).strip().capitalize()
    valorproduto = int(input('Valor do produto R$'))
    usuario = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    while usuario not in 'SN':
        usuario = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    contador = contador +1

    total = total + valorproduto

    if valorproduto > 1000:
        cont1000 = cont1000 +1

    if contador == 1:
        barato = valorproduto
        baratonome = nomeproduto
    else:
        if valorproduto < barato:
            barato = valorproduto
            baratonome = nomeproduto

    if usuario == 'N':
        print(f'Total da compra foi R${total:.2f}')
        print(f'Temos {cont1000} produtos custando mais de R$1000')
        print(f'Produto mais barato foi {baratonome} que custa R${barato:.2f}')
        break