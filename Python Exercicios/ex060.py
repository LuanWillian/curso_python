numero = int(input('Digite um numero para saber seu fatorial: '))
contador = numero
fatorial = 1
print('Calculando {}! = '.format(numero), end='')
while contador > 0:
    print('{} '.format(contador), end='')
    if contador > 1:
        print('x ',end='')
    else:
        print('= ',end='')
    fatorial = fatorial * contador
    contador = contador -1
print('{}'.format(fatorial))