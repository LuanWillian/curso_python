while True:
    strings = ('Um','Dois','Tres','Quatro','Cinco','Seis','Sete','Oito','Nove',
'Dez','Onze','Doze','Treze','Catoze','Quinze','Dezeses','Dezesete','Dezoito','Dezenove','Vinte')

    usuario = int(input('Digite um numero de 0 a 20: '))
    while usuario >= 20 or usuario <= 0:
        usuario = int(input('Tente Novamente! Digite um numero de 0 a 20: '))

    if usuario > 0:
        print(strings[usuario-1])

    op = str(input('Quer continuar? [N/S]: ')).strip().upper()
    if op == 'N':
        break
