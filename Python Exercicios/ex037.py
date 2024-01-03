num = int(input('Digite um numero inteiro: '))
print('''Escolha uma das bases para conversão:
[ 1 ] Converter para BINARIO
[ 2 ] Converter para OCTAL
[ 3 ] Converter para HEXADECIMAL''')

opção = int(input('Sua opção: '))

if opção == 1:
    print('{} convertido para BINARIO e: {}'.format(num, bin(num)[2:]))

elif opção == 2:
    print('{} convertido para OCTAL e: {}'.format(num, oct(num)[2:]))

elif opção == 3:
    print('{} convertido para HEXADECIMAL e: {}'.format(num,hex(num)[2:]))

else:
    print('Opção errada! Tente novamente')