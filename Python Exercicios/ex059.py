opçao = 0
while not opçao == 5:
    print('')
    valor1 = int(input('Digite o primeiro numero: '))
    valor2 = int(input('Digite o segundo numero: '))
    print('')
    print('''Escolha o que você quer fazer com os numeros:
[ 1 ] SOMAR  
[ 2 ] MULTIPLICAR
[ 3 ] MAIOR
[ 4 ] NOVOS NUMEROS
[ 5 ] SAIR DO PROGRAMA''')
    opçao = int(input('Qual a sua opção: '))
    print('')

    if opçao == 1:
        res = valor1 + valor2
        print('A soma dos numeros {} e {} foi {}'.format(valor1,valor2,res))

    elif opçao == 2:
        res = valor1 * valor2
        print('A multiplicação dos numeros {} e {} foi {}'.format(valor1,valor2,res))

    elif opçao == 3:
        if valor1 > valor2:
            maior = valor1
        if valor1 < valor2:
            maior = valor2
        print('O maior numero e {}'.format(maior))

    elif opçao == 4:
        print('Digite os numeros novamente')

    elif opçao == 5:
        print('Fim do pograma! Volte sempre!')

    else:
        print('Opção invalida Tente Novamente!')
