print('{:=^40}'.format(' Lojas Luan '))
from time import sleep
produto = float(input('Qual valor do produto R$'))

print('''Qual a forma de pagamento?
    [ 1 ] DINHEIRO OU CHEQUE
    [ 2 ] CARTÃO AVISTA
    [ 3 ] CARTÃO PARCELADO''')

opcao1 = int(input('Sua opção: '))
print('Processando...')
sleep(2)

if opcao1 > 3 or opcao1 < 1:
    print('Opçao não existe! Tente novamente')

if opcao1 == 1:
    valor = produto - (produto * 10 / 100)
    print('Seu produto de R${:.2f} teve um desconto de 10% que ao todo fica R${:.2f}'.format(produto, valor))

elif opcao1 == 2:
    valor = produto - (produto * 5 / 100)
    print('Seu produto de R${:.2f} teve um desconto de 5% que ao todo fica R${:.2f}'.format(produto, valor))

elif opcao1 == 3:
    opcao2 = int(input('Voce quer parcela em quantas vezes? *O LIMITE E DE 12x*: '))
    print('Processando...')
    sleep(2)

    if opcao2 == 2:
        print('Sua compra de R${:.2f} parcelada em 2x não teve descontos e nem juros!'.format(produto))

    elif opcao2 <= 12:
        valor2 = produto + (produto * 20 / 100)
        print('Seu produto de R${:.2f} vai ter um juros de 20% que ao todo fica R${:.2f}'.format(produto, valor2,))

    elif opcao2 > 12:
        print('Passou do limite de parcelas! Tente novamente!')
